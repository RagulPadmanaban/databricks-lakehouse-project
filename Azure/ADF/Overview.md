# 🚀 Azure Data Factory Projects

This section contains projects implemented using **Azure Data Factory (ADF)**, focusing on building scalable, production-ready data pipelines using modern data engineering practices.

---

## 📌 Overview

Azure Data Factory is used to design and orchestrate ETL/ELT pipelines.  
The projects in this section demonstrate:

- Dynamic pipeline design
- Metadata-driven architecture
- Data ingestion and transformation
- Parameterization across pipeline, data flow, and datasets
- Real-world data lake implementations

---

## 🧰 Technologies & Concepts Covered

- Azure Data Factory (ADF)
- Azure Data Lake Storage Gen2 (ADLS)
- Mapping Data Flow (Spark-based transformations)
- Integration Runtime (Compute layer)
- Metadata-driven pipelines
- Dynamic datasets and parameterization

---

## 📂 Available Projects

### 🔹 1. Metadata-Driven Dynamic Pipeline

📁 Path: `Azure/ADF/Metadata-Driven-Pipeline`

#### ✅ Description
A fully dynamic ETL pipeline that processes multiple datasets using a **metadata JSON file**.

#### ✅ Features
- Lookup + ForEach implementation
- Dynamic file processing
- Parameterized datasets and data flows
- Raw → Silver data pipeline
- Scalable architecture for multiple tables

#### ✅ Key Concepts
- `@item()` → Pipeline expression  
- `$parameter` → Data Flow expression  
- `@dataset()` → Dataset parameter binding  

---

## 🎯 Purpose

These projects are designed to demonstrate:

- Real-world ETL pipeline implementation
- Scalable and reusable design patterns
- Strong understanding of Azure data engineering concepts

---

## 🚀 Future Enhancements

- Bronze → Silver → Gold architecture
- Integration with Azure SQL / Databricks
- Logging and monitoring pipelines
- Error handling frameworks

---

## 💡 Notes

Each project includes:
- Detailed README
- Sample data
- Architecture screenshots
- ADF JSON definitions

---

## 👨‍💻 Author

Ragul P
