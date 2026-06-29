# Retail Source System Simulation

## Overview

In enterprise retail environments, Azure Data Factory (ADF) typically does not ingest data directly from application repositories or GitHub.

Instead, source systems such as ERP, POS, CRM, Inventory Management Systems, or Vendor Systems export files into a landing location every day.

To simulate this enterprise architecture, this project introduces a separate Retail_Source folder outside the GitHub repository.

---

## Project Architecture

Retail Source (Local)
        │
        ▼
Azure Data Factory (ADF)
        │
        ▼
Azure Data Lake Storage Gen2
(Bronze Layer)

---

## Why Retail_Source is outside GitHub

The Retail_Source directory represents operational source systems.

It is intentionally excluded from GitHub because production source systems are not part of application repositories.

The GitHub repository only contains sample datasets so anyone can clone and reproduce the project.

---

## Repository Datasets

datasets/

Purpose:

- Sample data
- Documentation
- Reproducibility

---

## Retail_Source

Retail_Source/

Purpose:

- Simulated ERP/POS exports
- ADF ingestion source
- Daily Full Loads
- Daily Incremental Loads

---

## Folder Structure

Retail_Source/

master/

customers/
    full_load/
    incremental/

products/

stores/

transactions/

orders/
    full_load/
    incremental/

order_items/
    full_load/
    incremental/

---

## Benefits

- Mimics enterprise architecture
- Separates operational data from source code
- Enables realistic Azure Data Factory pipelines
- Supports Full Load and Incremental Load ingestion
- Keeps GitHub repository lightweight

---

## Local Retail_Source Setup

The `Retail_Source` directory is intentionally **not included** in this GitHub repository.

In enterprise environments, Azure Data Factory (ADF) does not ingest data from application repositories. Instead, operational systems such as ERP, POS, CRM, or Inventory Management Systems export data into a dedicated landing location. This project simulates that architecture using a local `Retail_Source` directory.

### Directory Location

Create the `Retail_Source` folder as a **sibling** of the project repository.

Example:

```text
Projects/
│
├── Retail-Analytics-Platform/
└── Retail_Source/
```

### Folder Structure

```text
Retail_Source/
│
├── master/
│   ├── customers/
│   │   ├── full_load/
│   │   └── incremental/
│   ├── products/
│   └── stores/
│
└── transactions/
    ├── orders/
    │   ├── full_load/
    │   └── incremental/
    └── order_items/
        ├── full_load/
        └── incremental/
```

### Data Generation

The Python data generation framework automatically writes datasets to two locations:

1. `Retail-Analytics-Platform/datasets/`

   * Repository sample datasets
   * Version controlled
   * Used for project reproducibility

2. `Retail_Source/`

   * Simulated enterprise source system
   * Used as the source location for Azure Data Factory (ADF)

### Azure Data Flow

```
Retail_Source
      │
      ▼
Azure Data Factory (Copy Activity)
      │
      ▼
ADLS Gen2 Bronze Layer
      │
      ▼
Azure Databricks
```

This design closely mirrors how enterprise retail organizations ingest operational data into a cloud data platform.
