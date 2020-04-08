Gia-Bao HUYNH | [LinkedIN](https://www.linkedin.com/in/gbh198/) | DURING QUARANTIE TIME | [UDACITY Data Engineering NanoDegree](https://www.udacity.com/course/data-engineer-nanodegree--nd027)

# **SQL Data Modelling with PostgreSQL**

## Table of Contents
-	Preamble
-	Introduction
-	Data Source
- Schema Design
-	Project Template
-	How To Use
- Potential Bugs

## Preamble

This repo is my work for Data Modelling with PostgreSQL in UDACITY [Data Engineering NanoDegree](https://www.udacity.com/course/data-engineer-nanodegree--nd027). Thank you Udacity team for all the support you have provided. 

## Introduction

A startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their music streaming app. The analysis team wants to have a place to store and query data. Currently, all data generated are in JSON format residing in data stores on the app. PostgreSQL is a traditionally chosen solution.

A relational database like PostgreSQL is a good choice beacause of its features (ACID) which guarantee data consistency. These tried-and-true properties have always played an important role in the world of big data. ACID stands for Atomicity, Consistency, Isolation, Durability. [Find out more about ACID.](https://en.wikipedia.org/wiki/ACID).

When doing modelling with a relational database, a [3NF](https://en.wikipedia.org/wiki/Third_normal_form) arpproach is often opted with two biggest purposes: Ensuring Data Validaty & Saving Storage spaces.

However, time passes, people change, demands are varied. In modern life where people prefer speed of flash in data processing, a schema with too many joins (like 3NF approach) is not welcomed. Moreover, that cost of data storage is dramatically falling down motivated people to find out another approach other than 3NF. That's why "A Star (Schema) is Born".

// "A Star (Schema) is Born" is not composed by Lady Gaga.

[Star Schema](https://en.wikipedia.org/wiki/Star_schema) is optmized for fast READS by reducing times of travelling of DBMS through joins. I applied Star Schema to this small project. We accept data redundancy (but who cares when it's cheap) to win the game of speed. 
If our application is low in speed, we could potentially lose customers. This does hurt more.

It is my job, as a data engineer, to build ETL pipelines that **Extract** data from data sources (JSON format), then **Transform** them (Python DataFrame) into a pre-defined schema (Star Schema), and finally, **Load** all to PostgreSQL. 

## Data Source
Data sources, a subset of real data from the [Million Song Dataset](http://millionsongdataset.com/), are comprised of 2 folders. Two folders are used to separate two types of available data: **Song Data** (*info about songs and artists*), **Log Data** (*info about user’s activities*). 

All the files available in these two S3 buckets are in JSON format. For example:
- song_data/A/B/C/TRABCEI128F424C983.json
- song_data/A/A/B/TRAABJL12903CDCF1A.json

And below is an example of what the data in a log file, 2018-11-12-events.json, looks like.

![Image of Yaktocat](https://github.com/gbh198/Cloud-Data-Warehouse-With-Amazon-S3-and-Redshift/blob/master/log-data.png)

## Schema Design

Sparkify schema has a star design. This design is optimal for ad-hoc queries and understandable for users. 
Star design means that it has one Fact Table surrounded by Dimension Tables. 
The Fact Table will answer a business question. In case of Sparkify, Fact Tables is about: **“What songs are users listening to?”**.

![Image of Yaktocat](https://github.com/gbh198/Cloud-Data-Warehouse-With-Amazon-S3-and-Redshift/blob/master/Star%20Schema.png)

## Project Template

- **etl.ipynb** – All logical operations performed to process data
- **test.ipynb** – Place to test if operations in etl.ipynb worked well
-	**create_tables.py** – Dropping old tables and Creating new ones
-	**etl.py** – ETL process to Extract data from local directories (JSON format), then Transform and Load to PostgreSQL tables
-	**sql_queries.py** – Modular collection of SQL queries (grouped by functions)

## How To Use
**Required libraries**
- PostgreSQL installed 
- psycopg2
- panda

It is recommended to consult etl.ipynb before running python files.

1.	Setting your file system to root, navigate to the folders that contains python files, and execute following command in terminal:
**python create_tables.py** 
2.	Running your ETL process :
**python etl.py** 
3.	Running the analytic queries on your PosgreSQL database to compare your results with the expected results.

## Potential Bugs

1. Before re-running any cells in etl.ipynb, it is compulsory to run create_tables.py. This file will create a database for you to play with.
2. Order of queries in module create_table_queries in sql_queries.py could throw an error when creating tables. It is recommended to create tables having no foreign keys before all. 

