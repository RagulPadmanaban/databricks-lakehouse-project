# 🚀 Metadata-Driven Dynamic ETL Pipeline using Azure Data Factory

---

## 📌 Project Overview

This project implements a **dynamic, metadata-driven ETL pipeline** using **Azure Data Factory (ADF)**.

The pipeline is designed to process multiple files dynamically from the Raw layer and load the processed data into the Silver layer without any hardcoding.

All execution logic is controlled using a **metadata JSON file**, making the solution scalable and reusable.

---

## 🎯 Objective

- Build a reusable and scalable pipeline
- Eliminate hardcoding
- Dynamically handle multiple files
- Implement real-world ETL architecture (Raw → Silver)

---

## 🏗️ Architecture

```md

-This pipeline uses a metadata-driven approach to dynamically control source and destination paths.
- metadata.json → Lookup → ForEach → Data Flow → ADLS (Silver)

---

## 🧰 Technologies Used

- Azure Data Factory (ADF)
- Azure Data Lake Storage Gen2 (ADLS)
- Mapping Data Flow (Spark-based transformation)
- JSON (metadata configuration)

---

## 📁 Data Lake Structure

### 🟢 Raw Layer

datalake/raw/
├── customers.csv
└── orders.csv

---

### 🟡 Config Layer


datalake/config/
└── metadata.json

---

### 🔵 Silver Layer (Output)


datalake/silver/
├── customers/
│     └── customers.csv
└── orders/
└── orders.csv

---

## 📄 Metadata Configuration

```json
[
  {
    "source_file": "customers.csv",
    "source_path": "raw/",
    "sink_path": "silver/customers/"
  },
  {
    "source_file": "orders.csv",
    "source_path": "raw/",
    "sink_path": "silver/orders/"
  }
]
