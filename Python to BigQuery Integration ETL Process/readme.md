# E-commerce Superstore Data Analysis with BigQuery & Python

## 📌 Project Overview
This project showcases a complete data workflow for an E-commerce Superstore dataset using **Google Sheets**, **Python (Pandas)**, and **Google BigQuery**. The goal is to demonstrate how a data scientist can:

- Read data directly from Google Sheets
- Perform data cleaning and exploratory analysis
- Merge multiple datasets into a consolidated view
- Store the processed data in BigQuery
- Query and visualize data using SQL and Python

---

## 🧰 Tools & Libraries Used
- **Google Sheets** (as data source)
- **Python (Pandas, NumPy)** for EDA and data transformation
- **Google BigQuery** for storing and querying large-scale datasets
- **Google Colab** for cloud-based execution

---

## 🔗 Data Sources (Google Sheets as CSV)
The following Google Sheets were used and converted to CSV links:

- **Orders**  
  `https://docs.google.com/spreadsheets/d/1M0u00wa4A6CqTA8xImd90nDtF86OwhR2ESgQjUItfaY/export?format=csv&gid=1531479241`

- **Customers**  
  `https://docs.google.com/spreadsheets/d/1M0u00wa4A6CqTA8xImd90nDtF86OwhR2ESgQjUItfaY/export?format=csv&gid=2099175586`

- **Returns**  
  `https://docs.google.com/spreadsheets/d/1M0u00wa4A6CqTA8xImd90nDtF86OwhR2ESgQjUItfaY/export?format=csv&gid=1158708900`

- **Users**  
  `https://docs.google.com/spreadsheets/d/1M0u00wa4A6CqTA8xImd90nDtF86OwhR2ESgQjUItfaY/export?format=csv&gid=531959115`

---

## 📊 Exploratory Data Analysis (EDA)

Initial inspection revealed many missing values in the `Status` column:

```python
df_consolidated['Status'].value_counts(dropna=False)
```

**Output:**
```
NaN         9328
Returned      98
```

Missing values were interpreted as "Order Not Returned" and filled accordingly:

```python
df_consolidated['Status'] = df_consolidated['Status'].fillna('Order Not Returned')
```

---

## 🔄 Data Consolidation
Multiple tables were joined using appropriate keys to create a denormalized structure ideal for analysis. Key operations included:
- Merging `Orders` with `Customers` and `Returns`
- Mapping user-level data from `Users` sheet

---

## ☁️ Storing Data into BigQuery

The cleaned and consolidated dataset was written to a BigQuery table named `superstore_sales_denormalized_table` in the dataset `ecommerce_data`.

```python
df_consolidated.to_gbq(
    'ecommerce_data.superstore_sales_denormalized_table',
    project_id='tutorial-data-441413',
    if_exists='replace'
)
```

> ⚠️ Note: `to_gbq()` is deprecated. Future projects should use `pandas_gbq.to_gbq()` instead.

---

## 📥 Reading Back from BigQuery

Data can be retrieved back using SQL queries via Python:

```python
QUERY = 'SELECT * FROM tutorial-data-441413.ecommerce_data.superstore_sales_denormalized_table LIMIT 100'
query_job = client.query(QUERY)
df = query_job.result().to_dataframe()
```

**Sample Output:**
| Order ID | Product Category | Profit | Manager | Status             |
|----------|------------------|--------|---------|--------------------|
| 88525    | Office Supplies  | 1.32   | Chris   | Order Not Returned |
| 88522    | Office Supplies  | 4.56   | William | Order Not Returned |
| ...      | ...              | ...    | ...     | ...                |

---

## ✅ Key Outcomes
- ✅ Automated data ingestion from Google Sheets
- ✅ Comprehensive data cleaning & transformation
- ✅ Consolidated reporting table ready for BI
- ✅ Storage and querying via BigQuery for scalability

---

## 📌 Next Steps
- Add visualization dashboards using Looker Studio or Power BI
- Build ML models (e.g., return prediction) using BigQuery ML or scikit-learn
- Automate the data pipeline with Airflow or Cloud Functions

---

## 🧠 Author
**Tanim**  
Data Analyst | BI Consultant | Python & SQL Enthusiast

