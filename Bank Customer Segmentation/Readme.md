# 🏦 Bank Churn Customer Analysis: Customer Segmentation

## 📌 Overview
This project segments bank customers based on their financial and behavioral attributes to identify patterns and recommend personalized financial products or services. It employs **K-Means clustering** to group similar customers and derive actionable business insights.

## 🎯 Objectives
1. **Prepare the Data for Modeling**  
   - Select relevant fields and ensure numeric consistency.
   - Analyze distributions and engineer new features.
   
2. **Perform Customer Segmentation (Round 1)**  
   - Standardize the data.
   - Use K-Means clustering to identify customer groups.
   - Interpret cluster characteristics.

3. **Refine Customer Segmentation (Round 2)**  
   - Explore alternative feature selections.
   - Assess model performance using new subsets.

4. **Analyze Clusters & Provide Business Recommendations**  
   - Examine churn rates across clusters.
   - Tailor financial strategies for each segment.

---

## 📊 Dataset
The dataset includes customer attributes such as:
- `CreditScore`: Creditworthiness score.
- `Geography`: Customer's country of residence.
- `Gender`: Customer's gender (converted to numeric).
- `Age`: Customer’s age.
- `Tenure`: Years as a bank customer.
- `Balance`: Account balance.
- `NumOfProducts`: Number of products used.
- `HasCrCard`: Whether the customer has a credit card.
- `IsActiveMember`: Activity status.
- `EstimatedSalary`: Estimated income.
- `Exited`: Whether the customer left the bank (used for churn analysis).

---

## ⚙️ Methodology

### 📌 1. Data Preprocessing
✅ **Subset Selection:** Remove unnecessary fields (`CustomerId`, `Surname`, `Exited`).  
✅ **Feature Engineering:** Create new features (e.g., `ProductsPerYear`).  
✅ **Handling Categorical Data:** Convert categorical variables (`Gender`, `Geography`) into numeric form.  
✅ **Data Scaling:** Standardize numerical fields using `StandardScaler`.

### 📌 2. Exploratory Data Analysis (EDA)
✅ **Distribution Analysis:** Examine min/max values and visualizations for each attribute.  
✅ **Correlation Analysis:** Identify key relationships between features.

### 📌 3. K-Means Clustering (Round 1)
✅ **Standardization:** Ensure uniform scaling across all features.  
✅ **Elbow Method:** Determine optimal cluster count using an inertia plot.  
✅ **Model Fitting:** Train K-Means models with 2-15 clusters and evaluate inertia & silhouette scores.  
✅ **Cluster Analysis:** Interpret segment characteristics.

### 📌 4. K-Means Clustering (Round 2)
✅ **Feature Selection Adjustment:** Exclude `Geography` to avoid country-based dominance.  
✅ **New Cluster Insights:** Compare model performance with the revised dataset.

### 📌 5. Insights & Business Recommendations
✅ **Churn Analysis:** Identify clusters with high churn rates.  
✅ **Country-wise Breakdown:** Compare customer distributions per geography.  
✅ **Personalized Strategies:** Recommend tailored financial products.

---

## 📈 Results & Key Findings

### 🔍 Identified Clusters
1. **Cluster 0:** Customers who don't have a credit card.  
2. **Cluster 1:** High balance customers with few products and a credit card.  
3. **Cluster 2:** Low balance customers with multiple products and a credit card.  
4. **Cluster 3:** Customers who acquire many products in a short period.  

### 🔥 Business Recommendations
- **Cluster 0:** Introduce an entry-level credit card; analyze demographic details.  
- **Cluster 1:** Retain high-balance customers with investment opportunities & financial advisory services.  
- **Cluster 2:** Reward loyal customers (French & Spanish) with incentives and exclusive product offers.  
- **Cluster 3:** Extend product tenure options to maximize retention.

---

## 🛠️ Technologies Used
- **Python** 🐍
- **Pandas & NumPy** (Data Processing)
- **Matplotlib & Seaborn** (Data Visualization)
- **Scikit-Learn** (Machine Learning Models for Clustering)

---

