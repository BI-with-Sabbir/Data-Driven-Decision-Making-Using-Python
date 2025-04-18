# Python to BigQuery ETL Pipeline Project

## 📅 Project Overview
This project demonstrates a complete **ETL (Extract, Transform, Load)** pipeline using Python, Google Sheets, and Google BigQuery. It includes data extraction from Google Sheets, data cleaning and transformation in Python, and loading the consolidated data into BigQuery for further analysis. A stored procedure is also created in BigQuery to remove records with negative profit.

---

## 💰 Data Sources
All data is retrieved directly from a shared **Google Spreadsheet**, which includes multiple sheets:

| Sheet Name | Description | CSV Link |
|------------|-------------|----------|
| Orders     | Contains sales transaction records | [Orders CSV](https://docs.google.com/spreadsheets/d/1M0u00wa4A6CqTA8xImd90nDtF86OwhR2ESgQjUItfaY/export?format=csv&gid=1531479241) |
| Customers  | Maps Customer IDs to Names | [Customers CSV](https://docs.google.com/spreadsheets/d/1M0u00wa4A6CqTA8xImd90nDtF86OwhR2ESgQjUItfaY/export?format=csv&gid=2099175586) |
| Returns    | Indicates which orders were returned | [Returns CSV](https://docs.google.com/spreadsheets/d/1M0u00wa4A6CqTA8xImd90nDtF86OwhR2ESgQjUItfaY/export?format=csv&gid=1158708900) |
| Users      | Associates regions with sales managers | [Users CSV](https://docs.google.com/spreadsheets/d/1M0u00wa4A6CqTA8xImd90nDtF86OwhR2ESgQjUItfaY/export?format=csv&gid=531959115) |

---

## 🌐 Tech Stack
- **Python**: `pandas`, `numpy`, `matplotlib`, `seaborn`
- **Google BigQuery**: for storing and querying consolidated data
- **Google Sheets**: for initial data source

---

## 📊 ETL Steps

### ✂️ Extract
- Data is fetched directly using `pandas.read_csv()` with a converted CSV export link from Google Sheets.

### ⚖️ Transform
- Data type conversions (e.g., dates, postal codes)
- Cleaning missing or incorrect values
- Joining multiple sheets:
  - Orders ➔ Customers
  - Orders ➔ Users
  - Orders ➔ Returns
- Statistical summaries using `.describe()` and `.info()`

### ↓ Load
- The cleaned and consolidated data is pushed into **Google BigQuery** using `to_gbq()`.

```python
from pandas_gbq import to_gbq

df_consolidated.to_gbq(
    destination_table='ecommerce_data.superstore_sales_denormalized_table',
    project_id='tutorial-data-441413',
    if_exists='replace'
)
```

---

## 📊 BigQuery Stored Procedure
A stored procedure was created to **remove rows where profit is negative**.

### Stored Procedure:
```sql
CREATE OR REPLACE PROCEDURE `tutorial-data-441413.ecommerce_data.remove_negative_profits`(
    IN table_name STRING
)
BEGIN
  DELETE FROM `tutorial-data-441413.ecommerce_data.superstore_sales_denormalized_table`
  WHERE Profit < 0;
END;
```

### Call Procedure from Python:
```python
client.query("CALL `tutorial-data-441413.ecommerce_data.remove_negative_profits`('superstore_sales_denormalized_table')")
```

---

## 🔄 Retrieve Data from BigQuery
To read data back into Python:
```python
from google.cloud import bigquery

client = bigquery.Client(project='tutorial-data-441413')
query = """
    SELECT * FROM `tutorial-data-441413.ecommerce_data.superstore_sales_denormalized_table`
    LIMIT 100
"""

df = client.query(query).to_dataframe()
```

---

## 📑 Key Learnings
- Seamless integration between Google Sheets and Python
- Data transformation & type casting with Pandas
- Working with Google BigQuery in Python
- Creating and executing stored procedures from Python

---

## 🏆 Final Output
- Cleaned and merged dataset stored in BigQuery.
- Ready for advanced analytics and dashboarding in tools like **Looker Studio**, **Power BI**, etc.

---


