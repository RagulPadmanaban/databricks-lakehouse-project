# 🚀 Dynamic Incremental Data Pipeline (Databricks)

## 📌 Overview
This project implements a dynamic, metadata-driven incremental data pipeline using Databricks and PySpark.

The pipeline processes only new data based on a watermark (last_processed_date) and performs upsert operations using Delta Lake.

---

## 🧠 Key Concepts Implemented

- Metadata-driven pipeline  
- Incremental data loading  
- Dynamic table handling  
- MERGE (upsert) logic  
- Delta Lake storage  

---

## ⚙️ Architecture

Raw Data (CSV)  
      ↓  
Metadata Table (Watermark)  
      ↓  
Incremental Filter  
      ↓  
Delta Table (Silver Layer)  

---

## 📂 Workflow

### 1. Metadata Table Creation
Stores:
- table_name  
- source_path  
- last_processed_date  
- target_table  

---

### 2. Read Metadata
Extract:
- Source path  
- Last processed date  
- Target table name  

---

### 3. Incremental Load
- Read source CSV  
- Filter using:
```
order_date > last_processed_date
```

---

### 4. Write to Delta Table
- Append new data to Silver layer  

---

### 5. Upsert using MERGE
- Match condition:
```
order_id
```
- Update existing records  
- Insert new records  

---

### 6. Update Metadata
- Calculate:
```
max(order_date)
```
- Update metadata table with latest processed date  

---

## 🧪 Technologies Used

- Databricks (Community Edition)  
- PySpark  
- Delta Lake  

---

## 🔄 Features

- Dynamic pipeline (no hardcoded logic)  
- Incremental processing using metadata  
- Idempotent design (safe re-runs)  
- Scalable for multiple tables  

---

## 📊 Output

- Only new data is processed  
- Existing records are updated  
- Metadata is updated with latest processed date

## 📷 Pipeline Output

### Delta Table (Silver Layer)
![Delta](screenshots/deltatable.png)

### Incremental Load Execution
![Incremental](screenshots/incremental_pipeline.png)

### Metadata Update (Watermark)
![Metadata](screenshots/metadata_update.png)

---

## 🚀 How to Run

1. Upload CSV to:
```
/Volumes/.../raw/
```

2. Run the notebook  

3. Pipeline will:
- Load new data  
- Merge into Delta table  
- Update metadata automatically  

---

## 📷 Future Improvements

- Multi-table processing loop  
- SCD Type 2 implementation  
- Data quality validation  
- Streaming integration  

---

## 💬 Interview Explanation

“I built a metadata-driven incremental data pipeline in Databricks that dynamically processes new data using a watermark and performs upserts using Delta Lake MERGE.”
