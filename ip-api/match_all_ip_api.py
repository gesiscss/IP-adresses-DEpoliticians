import pandas as pd
import requests as r
import time
from sqlalchemy import create_engine
from ratelimit import rate_limited
from tqdm import tqdm, tqdm_pandas

tqdm.pandas()


df_officials = pd.read_csv('NEW_officials_total_actions.csv', index_col=0)
all_off_article_ids_str = str(tuple(df_officials['article_id'].unique()))

engine = create_engine('postgresql://postgres:4vtqqCjpTKsVG46i@193.175.238.88:5432/ww_api_live')
edits_by_all =pd.read_sql_query('SELECT editor_name, article_id, year_month, id from "wikiwho_editordatade" WHERE editor_id = 0 AND article_id in'  
                                      + all_off_article_ids_str ,con=engine)
@rate_limited(2.5)
def get_origin_ip_api(x):
    for i in range(1,6):
        try:
            resp = r.get("http://ip-api.com/json/" + x)
            data = resp.json()
            if "org" in data:
                return data['org']
            return False
        except Exception:
            time.sleep(i)
            continue
    print('failed')
    return 'unmatched'

edits_by_all['ip_api_origin'] = edits_by_all["editor_name"].progress_apply(get_origin_ip_api)   
edits_by_all[['id', 'ip_api_origin']].to_csv('ip_api_origin_all.csv')