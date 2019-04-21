## Task: Using the [ip-api](http://ip-api.com) to get meta data about IPs of editors

File: ip-api matching.ipynb

### Part 1: Query ip-api for known government IP addresses
In the first section, we query the ip-api passing known government IP addresses. This is done to determine if the list of IP ranges acquired from [bund-networks](https://github.com/codemonauts/bundesedit/blob/master/bund-networks.json) is relevant and up to date.

### Part 2: Query ip-api on articles edited by officials
To increase the number of results, we use all edits done by anonymous editors on articles that were edited by officials. The information about officials come from prevoiusly mentioned bund-networks.

File: ip-api analysis.ipynb
### Part 1: Compare bund-networks with ip-api, officials' edits only
We group the dataframe by the bund-networks origin, and list all the corresponding entries from ip-api on the right side

### Part 2: Compare bund-networks with ip-api, articles edited by officials
After matching all edits performed on articles edited by officials, we now check for those that match to our regex list used in RIPE.