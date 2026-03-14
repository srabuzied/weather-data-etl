# Weather Data ETL Pipeline

An end to end ETL pipeline that extracts weather forecast data from a REST API in JSON format, converts it to CSV using Python, and processes it with Talend Open Studio to generate structured analytical datasets.

## Overview
This project demonstrates a complete ETL workflow for processing weather forecast data.  
Data is extracted from a REST API, preprocessed using a Python script `converter.py`, and then processed through a Talend ETL pipeline where transformations, replication, aggregation, and sorting are performed to produce clean analytical datasets.

## Architecture

Weather REST API JSON  
↓  
Python preprocessing script `converter.py`  
↓  
Talend Open Studio ETL workflow  
- tMap for data transformation  
- tReplicate for data branching  
- tAggregateRow for aggregation  
- tSortRow for sorting  
↓  
Output datasets

## Technologies
- Python  
- Talend Open Studio  
- REST API  
- CSV data processing  
- ETL pipeline design  

## Repository Structure

weather-data-etl  
│  
├ data/          # Raw and processed datasets  
├ scripts/       # Python preprocessing script  
├ talend/        # Talend ETL workflow  
├ screenshots/   # Pipeline diagram  
└ README.md  


## Outputs
- `weatherOut.csv` – cleaned weather dataset  
- `weatherSummary.csv` – aggregated weather statistics  

## Pipeline Diagram
![Pipeline](screenshots/pipeline.png)
