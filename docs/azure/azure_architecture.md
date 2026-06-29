# Azure Architecture

## Overview

The Retail Analytics Platform follows the Medallion Architecture (Bronze, Silver, and Gold) using Azure cloud services. The project simulates a real-world retail data engineering pipeline where historical and daily incremental data are generated locally, ingested into Azure, transformed using Databricks, and finally prepared for reporting and analytics.

---

# End-to-End Architecture

```
                    Local Machine
                           │
                           │
          Simulated Retail Source System (Python)
                           │
       Full Load & Incremental CSV Exports
                           │
                           ▼
                Azure Data Factory (ADF)
             Copy Activity / Orchestration
                           │
                           ▼
        Azure Data Lake Storage Gen2
                 Bronze Layer
                           │
                           ▼
             Azure Databricks (PySpark)
      Data Validation, Cleansing & Standardization
                           │
                           ▼
        Azure Data Lake Storage Gen2
                 Silver Layer
                           │
                           ▼
             Azure Databricks (PySpark)
      Business Transformations & Data Modeling
                           │
                           ▼
        Azure Data Lake Storage Gen2
                  Gold Layer
                           │
                           ▼
                     Power BI
```

---

# Data Flow

## 1. Source System

The project begins with a simulated retail source system developed in Python. The source system generates realistic master and transactional datasets.

### Master Data

- Customers
- Products
- Stores

### Transaction Data

- Orders
- Order Items

Both historical and incremental datasets are produced.

---

## 2. Azure Data Factory

Azure Data Factory acts as the ingestion and orchestration service.

Responsibilities include:

- Historical data ingestion
- Incremental data ingestion
- Pipeline orchestration
- Scheduling
- Monitoring pipeline execution

ADF copies source CSV files into Azure Data Lake Storage Gen2.

---

## 3. Bronze Layer

The Bronze layer stores raw source-system data exactly as received.

Characteristics:

- No transformations
- Original schema preserved
- Source system defects retained
- Historical and incremental loads stored

Example:

```
bronze/

    master/
        customers.csv
        products.csv
        stores.csv

    transactions/
        orders.csv
        order_items.csv
```

---

## 4. Silver Layer

Azure Databricks reads Bronze data and performs data engineering transformations.

Typical operations include:

- Schema validation
- Null handling
- Duplicate removal
- Invalid record handling
- Data type standardization
- Business rule validation
- Quality reporting

The Silver layer contains trusted, cleansed data.

---

## 5. Gold Layer

The Gold layer contains analytics-ready datasets.

Examples include:

- Customer Analytics
- Product Analytics
- Store Analytics
- Sales Analytics
- Revenue KPIs

The Gold layer is optimized for reporting and business intelligence.

---

## 6. Power BI

Power BI connects to the Gold layer.

Business users consume dashboards including:

- Daily Sales
- Revenue
- Customer Segments
- Product Performance
- Store Performance

---

# Azure Services

| Service | Purpose |
|----------|---------|
| Azure Resource Group | Resource management |
| Azure Data Lake Storage Gen2 | Data lake |
| Azure Data Factory | Data ingestion |
| Azure Databricks | Data transformation |
| Azure Key Vault | Secret management |
| Managed Identity | Secure authentication |
| Log Analytics Workspace | Monitoring |
| Power BI | Reporting |

---

# Medallion Architecture

```
    Source System
        │
        ▼
Bronze (Raw Data)
        │
        ▼
Silver (Cleansed Data)
        │
        ▼
Gold (Business Ready Data)
        │
        ▼
     Power BI
```

---

# Current Project Status

| Layer | Status |
|---------|--------|
| Source System | Completed |
| Bronze | Planned |
| Silver | Planned |
| Gold | Planned |
| Power BI | Planned |

---

# Phase

Phase 2 - Azure Environment Setup

Story 1 - Azure Resource Group & Naming Convention
