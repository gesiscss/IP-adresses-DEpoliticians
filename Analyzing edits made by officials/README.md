## Task: Analyze Wikipedia edits made by German officials

### Legend

Data sources:  
BUND - 
RIPE -

### Part 1: Data gathering
#### Notebook: Categories(politik) for articles edited by officials.ipynb

For all articles edited by the officials (based on RIPE data), we get the category for every article. If the article category contains the word "politik", we set the field politik to true.

#### Notebook: German Parlament members extraction.ipynb

We use the wikipedia pages of [German parlament assembly](https://de.wikipedia.org/wiki/Liste_der_Mitglieder_des_Deutschen_Bundestages_(19._Wahlperiode)) to gather links of Parlament members in the last 5 assemblies (15-19).

//TODO save the party of every politician

#### Notebook: get_revision_ids_OLD.ipynb

This notebook was a part of a pipeline for getting revision IDs for BUND data. It can be used to get revisions from data present in our wikiwhodata database.

### Part 2: Analysis of officials actions on parlament member pages

#### Notebook: Member pages - all edits BUND.ipynb

We look into edits made on pages of parlament members, done by officials (BUND).

#### Notebook: Member pages - all edits RIPE.ipynb

We look into edits made on pages of parlament members, done by officials (RIPE).

### Part 3: Analysis of officials total actions on all articles

#### Notebooks: Survival of officials' actions BUND.ipynb, Survival of officials' actions RIPE.ipynb

We first look into the distribution of the success rate of officials (number of actions that survive 48h divided by total actions) over all wikipedia articles they edited. We take into account only articles with at least MIN_ACTIONS (default 100).

Secondly we take into account only the edits done on pages of parlament members. For these edits we show the success rate, grouped by party and normalized by number of members of a party.

Third, we show the number of actions on parlament member pages, grouped by party and normalized by number of members.

Last, we group all edits by the half year they were made in. We show the success rate of edits made by officials with more than 100 actions over a half year in an article. Then, for every half year we display the success rate for officials and all editors over wikipedia articles.

### Part 4: Analysis of officials all actions on all articles

#### Notebooks: Survival of officials' adds, dels, reins over time BUND.ipynb, Survival of officials' adds, dels, reins over time RIPE.ipynb

First graph shows the percentage of actions performed by officials over all editors, per action type (original add, reinsertion, deletion) over time.

Second graphs shows the percentage of officials' actions that are additions, reinsertions and deletion, over time. This is followed by the graph for all editors.

Graph four shows the success rate of all editors on articles edited by Officials.

In the next three graphs we show the success rate of additions, reinsertion and deletions for officials and all editors, over time.

Success rate of total actions on articles edited by Officials, over time.

Action type as a percentage of all actions - Officials and All editors

Half years

