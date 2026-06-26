# Azure Naming Convention

## Overview

This project follows a consistent Azure resource naming convention to simulate enterprise cloud governance and improve resource organization.

---

## Environment

| Environment | Abbreviation |
|-------------|--------------|
| Development |      dev     |

---

## Resource Naming Standards

|     Azure Resource      |        Naming Pattern       |        Planned Name     |
|-------------------------|-----------------------------|-------------------------|
| Resource Group          | rg-<project>-<environment>  | rg-retailanalytics-dev  |
| Storage Account         | st<project><environment>    | stretailanalyticsdev    |
| Azure Data Factory      | adf-<project>-<environment> | adf-retailanalytics-dev |
| Azure Databricks        | dbw-<project>-<environment> | dbw-retailanalytics-dev |
| Key Vault               | kv-<project>-<environment>  | kv-retailanalytics-dev  |
| Managed Identity        | mi-<project>-<environment>  | mi-retailanalytics-dev  |
| Log Analytics Workspace | log-<project>-<environment> | log-retailanalytics-dev |

---

## Azure Region

Central India

---

## Naming Guidelines

- Use lowercase letters.
- Use hyphens where Azure supports them.
- Storage account names must be lowercase and contain no special characters.
- Include the environment name for every Azure resource.
- Use consistent names across all Azure services.

---

## Benefits

- Consistent resource organization
- Easy identification of Azure services
- Improved governance
- Easier automation and deployment
- Enterprise-ready project structure
