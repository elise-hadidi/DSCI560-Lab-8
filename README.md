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
│   └── analysisCluster.py
├── README.md
└── requirements.txt
```

## Files
- Scripts/w2vBOW.py: Generates document embeddings using Word2Vec + Bag-of-Words method.
- Scripts/analysisCluster.py: Runs the Doc2Vec pipeline to generate document embeddings using different parameter configurations.
- Data/output.csv: Contains the Reddit posts exported from the database in the previous lab. This file is used as the main dataset for generating embeddings and running clustering experiments.
- Data/mydb.duckdb: The DuckDB file created in the previous lab that stores the scraped Reddit posts in a table and serves as the source of the data exported to output.csv

## Requirements
### Install dependencies with:
```
pip install -r requirements.txt
```

## Running the Pipeline
Step 1 – Generate Doc2Vec embeddings:
```
python3 Scripts/analysisCluster.py 
```

Step 2 – Generate Word2Vec + Bag-of-Words embeddings:
```
python3 Scripts/w2vBOW.py Data/output.csv Data/w2v_bow_output.csv <num_bins>
```
