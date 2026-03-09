# DSCI560-Lab-8

**Team Members:** Elise Hadidi (1137648541), Jordan Davies (1857892197), Ryan Silva (6463166471) 
**Team Number:**  17

## Overview
This project explores different ways to turn Reddit posts into embeddings for clustering and analysis. We test three different Doc2Vec configurations and compare them with a Word2Vec + Bag-of-Words approach to see which method better captures the meaning of the posts.

## Folder Structure
```
DSCI560-Lab-5/
├── Data/
│   ├── output.csv
│   └── mydb.duckdb
├── Scripts/
│   ├── w2vBOW.py
│   └── OTHER SCRIPT.py
├── README.md
└── requirements.txt
```

## Requirements
### Install dependencies with:
```
pip install -r requirements.txt
```

## Building the Database
Before running the automation script, you need to populate the database by scraping subreddits. Run from the project root (DSCI560-Lab-8/):
```
python3 Scripts/scrapeReddit.py <subreddit> <num_posts>
```
Example:
```
python3 Scripts/scrapeReddit.py cybersecurity 500
```
You can run this multiple times with different subreddits to combine data in the same database. The database file will be created at Data/mydb.duckdb. 

## How to Run
Once the database has been populated, run the automation script from the project root (DSCI560-Lab-8/):
```
python3 Scripts/automation.py <interval_minutes> 
```
Example:
```
python3 Scripts/automation.py 5 
```
- interval_minutes: how often to scrape and re-cluster
