# Azure Resource Group

## Overview

The Resource Group is the logical container for all Azure resources used in the Retail Analytics Platform. It provides centralized management, access control, monitoring, and lifecycle management for the project.

---

## Resource Group Details

| Property | Value |
|----------|-------|
| Resource Group Name | rg-retailanalytics-dev |
| Azure Region | Central India |
| Environment | Development |
| Project | Retail Analytics Platform |

---

## Resource Group Tags

| Tag | Value |
|-----|-------|
| Project | RetailAnalyticsPlatform |
| Environment | Development |
| Owner | Krishna |
| Purpose | Azure Data Engineering Learning |

---

## Azure Services

The following Azure services will be deployed inside this Resource Group during Phase 2.

| Service | Purpose |
|----------|---------|
| Azure Data Lake Storage Gen2 | Store Bronze, Silver, and Gold data layers |
| Azure Data Factory | Data ingestion and orchestration |
| Azure Databricks | Data transformation using PySpark |
| Azure Key Vault | Secure secrets and connection strings |
| Managed Identity | Secure authentication between Azure services |
| Log Analytics Workspace | Centralized monitoring and diagnostics |

---

## Benefits of Using a Resource Group

- Centralized resource management
- Simplified access control using Azure RBAC
- Unified monitoring and diagnostics
- Easier deployment and cleanup
- Better organization of cloud resources

---

## Future Architecture

```
Retail Source System
        │
        ▼
Azure Data Factory
        │
        ▼
Azure Data Lake Storage Gen2 (Bronze)
        │
        ▼
Azure Databricks
        │
        ▼
Azure Data Lake Storage Gen2 (Silver)
        │
        ▼
Azure Databricks
        │
        ▼
Azure Data Lake Storage Gen2 (Gold)
        │
        ▼
Power BI
```

---

## Current Status

| Azure Resource | Status |
|----------------|--------|
| Resource Group | Planned |
| ADLS Gen2 | Not Created |
| Azure Data Factory | Not Created |
| Azure Databricks | Not Created |
| Azure Key Vault | Planned |
| Managed Identity | Planned |
| Log Analytics Workspace | Planned |

---

## Story

Phase 2 - Sprint 1

Story 1 - Azure Resource Group & Naming Convention
