## Task: Get IP addresses of German government institutions - RIPE
Insights: 
1. RIPE has more fine-grained data than ip-api  
After gathering RIPE data (based on [bund-networks](https://github.com/codemonauts/bundesedit/blob/master/bund-networks.json), we matched all the edits from all the articles mentioned in RIPE. Comparing the results from RIPE and ip-api, we found no records that ip-api found and RIPE didnt. For some of the results RIPE had better and more up to date data.
2. RIPE contains all data from bund-networks, and even more  
RIPE data contains all ip ranges mentioned in bund-networks. RIPE also identified some bund-networks entries that are no longer valid.

Notebook: RIPE - getting new IPs.ipynb
### Part 1: Query ripe for known government IP addresses

In the first section, we query the RIPE api passing known government IP addresses. This is done to determine if the list of IP ranges acquired from [bund-networks](https://github.com/codemonauts/bundesedit/blob/master/bund-networks.json) is relevant and up to date.

All information about the ip ranges is saved in a dataframe. As the field "descr" has several entries, they are saved together separated by a "|" symbol.

#### Part 1.1 Comparison of RIPE entries for begining and end of an IP range

#### Part 1.2 Identification of entries that are no longer assigned to the institution


### Part 2: Query RIPE for organizations

As many RIPE IP entries do not have full information (missing 'netname' or 'descr'), and we cannot query organization names (API limitation), we first identify all organizations that match our keywords. 

Our keywords include all organizations from this wikipedia list: [Liste der deutschen Bundesbehörden](https://de.wikipedia.org/wiki/Liste_der_deutschen_Bundesbeh%C3%B6rden)

The keywords are saved in "RIPE_api_query_terms.txt", in a format that works with the API.

**Warning:** the list of organizations acquired here contains German, Austrian and (maybe) Swiss entries. 

A list of manually identified German organizations is saved in "RIPE_organizations.txt".

All the identified organizations (DE, AU, CH) are saved in "RIPE_orgs_query.txt".

### Part 3: Query RIPE for keywords
Using the list of keywords saved in the file, together with the list of organizations produced by part 2, all intenum(IPv4) and inet6num(IPv6) addresses are downloaded. The query is set to test all field for the given keywords. Field *country* is set to "DE", which eliminates all non German results (like the Austrian ones added in the part 2).

Duplicate results are removed based on the field *primary_key*.

At this point, downloaded results contain entries that dont belong to German official institutions (i.e. they contain *Bundes* in their name). They are removed using the regexes stored in "RIPE_regex_terms_RIPE.txt". These regexes are matched against fields *descr* and *netname*. The field *org* is matched against the list of manually found German institutions. - Change this to match to all, makes more sense

An entry is kept if it matches the regexes on **at least one** of the fields.

Field *name* is created to perserve all existing information about the entry (if exists: netname, descr, org), separated by "|".

### Part 4: Checking regexes against the list of institutions
Check if the regexes remove a result that should have been kept

### Part 5: Checking query terms against the list of institutions
Check if the query terms miss any of the institutions

### Part 6: Save to file
Save output to file "RIPE_ip_ranges.csv"

Notebook: RIPE_ip_matching.ipynb
### Part 1: Loading the RIPE ip ranges

### Part 2: Preparing data for matching
Python ipaddress package is used to handle IPv6 networks. 
For IPv4 addresses, we split the string representation into a tuple of 4 numbers.
192.168.1.1 -> (192, 168, 1, 1)
We perform basic data cleaning by removing entries that:
1. Have no ip address
2. IP address is in an invalid format (we assume that IPv4 addresses are contained from digits and a dot. For IPv6 we assume the address contains one ":")

### Part 3: Matching the wiki data against our IP ranges
To match IPv4 addresses, we expect the value to be inside of the IP range.
For IPv6 addresses, we use the IPv6Network object from module ipaddress
We save these results to a file.