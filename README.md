# Retail Analytics Platform

## Overview

Retail Analytics Platform is a production-style Data Engineering project that simulates a modern retail organization's analytics ecosystem.

The project is being built using an incremental, sprint-based approach and demonstrates:

* Master and Transaction Data Generation
* Full and Incremental Data Loading
* Watermark-Based Processing
* Business Realistic Data Simulation
* Data Quality and Validation Frameworks
* Azure Data Lake Architecture
* Azure Data Factory Pipelines
* Azure Databricks Transformations
* Reporting and Analytics

The long-term goal is to build an end-to-end Azure Data Platform using industry-standard Data Engineering practices.


## Technologies

- Azure Data Factory
- Azure Data Lake Storage Gen2
- Azure Databricks
- SQL
- Python
- PySpark

## Project Structure

Retail-Analytics-Platform
│
├── datasets
│   ├── master
│   └── transactions
│
├── scripts
├── logs
├── adf
├── databricks
├── sql
├── architecture
├── screenshots
└── docs


## Status

Phase 1 - Project Initialization

## Phase 1 Completed

- GitHub repository setup
- Dataset generation framework
- Customer master dataset
- Product master dataset
- Store master dataset
- Orders fact dataset
- Order Items fact dataset
- Architecture v1

## Phase 1.5 - Sprint 1 Completed

### Business Realism Enhancements
- Weighted payment method distribution
- Customer segment influence on order generation
- City-based order concentration
- Pareto product sales distribution

### Validation Results
- UPI ≈ 55% of transactions
- Platinum customers generate highest order volume
- Tier-1 cities generate most sales
- Top 20% products contribute ≈ 83% of revenue


### Phase 1.5 - Sprint 2 Completed

#### Incremental Load Framework

* Watermark-based processing
* Incremental customer onboarding
* Incremental order generation
* Incremental order item generation
* Validation framework
* Full vs Incremental execution modes

#### Incremental Datasets

* customers_incremental.csv
* orders_incremental.csv
* order_items_incremental.csv

#### Features Implemented

* Full Load Execution
* Incremental Load Execution
* Watermark Tracking
* Incremental Data Generation
* Schema Validation
* Primary Key Validation
* Incremental Processing Framework



## Execution

### Full Load | ###Incremental | ###validate

```bash
python scripts/generate_retail_data.py full

python scripts/generate_retail_data.py incremental

python scripts/generate_retail_data.py validate

```


## Roadmap

### Completed

✅ Phase 1 - Foundation

✅ Phase 1.5 Sprint 1 - Business Realism

✅ Phase 1.5 Sprint 2 - Incremental Load Framework

### Upcoming

⬜ Phase 1.5 Sprint 3 - Data Quality Simulation

⬜ Phase 1.5 Sprint 4 - Code Refactoring & Modularization

⬜ Phase 2 - Azure Environment Setup
- Azure Resource Group
- Azure Data Lake Storage Gen2
- Azure Data Factory
- Azure Databricks
