# 🏦 Bank Churn Customer Analysis: Customer Segmentation  
<img width="442" height="120" alt="Untitled Diagram drawio (2)" src="https://github.com/user-attachments/assets/bdb5a566-df94-4851-a159-87d342bbf730" />




![image](https://github.com/user-attachments/assets/73943f63-3daa-4c7d-aacd-049011ede6df)

## 🔗 Context Navigation

* [📌 Overview](#-overview)
* [🎯 Objectives](#-objectives)
* [📊 Dataset](#-dataset)
* [⚙️ Methodology](#️-methodology)
* [📈 Results & Key Findings](#-results--key-findings)
* [🛠️ Technologies Used](#-technologies-used)

---

## 📌 Overview

This project segments bank customers based on their financial and behavioral attributes to identify patterns and recommend personalized financial products or services. It employs **K-Means clustering** to group similar customers and derive actionable business insights.

---

## 🎯 Objectives

1. **Prepare the Data for Modeling**

   * Select relevant fields and ensure numeric consistency.
   * Analyze distributions and engineer new features.
     ![image](https://github.com/user-attachments/assets/71e7f58d-81fe-43be-9037-77369841c8c1)

2. **Perform Customer Segmentation (Round 1)**

   * Standardize the data.
   * Use K-Means clustering to identify customer groups.
   * Interpret cluster characteristics.
     ![image](https://github.com/user-attachments/assets/54e654c7-67d9-429c-bcf5-cc4991e82b60)

3. **Refine Customer Segmentation (Round 2)**

   * Explore alternative feature selections.
   * Assess model performance using new subsets.
     ![image](https://github.com/user-attachments/assets/539b0bec-c713-487b-ad0b-49d93fafb7d0)

4. **Analyze Clusters & Provide Business Recommendations**

   * Examine churn rates across clusters.
   * Tailor financial strategies for each segment.
     ![image](https://github.com/user-attachments/assets/f852fde6-a219-4e80-b00d-132388135dad)

---

## 📊 Dataset

![image](https://github.com/user-attachments/assets/293af4c1-51cd-459e-92b1-78bcc4b261f1)

The dataset includes customer attributes such as:

* `CreditScore`: Creditworthiness score
* `Geography`: Customer's country of residence
* `Gender`: Customer's gender (converted to numeric)
* `Age`: Customer’s age
* `Tenure`: Years as a bank customer
* `Balance`: Account balance
* `NumOfProducts`: Number of products used
* `HasCrCard`: Whether the customer has a credit card
* `IsActiveMember`: Activity status
* `EstimatedSalary`: Estimated income
* `Exited`: Whether the customer left the bank (used for churn analysis)

---

## ⚙️ Methodology

[📄 Click here To See Python NoteBook](https://github.com/BI-with-Sabbir/Data-Driven-Decision-Making-Using-Python/blob/main/Bank%20Customer%20Segmentation/Bank%20Customer%20Segmentation.pdf)

### Steps to Building ML Model

* Preparing the Data for Modeling
* Making Text Fields Numeric
* Exploring the Data
* Feature Engineering
* Scale the Data using Standardization
* Fit K-Means Models with 2–15 Clusters
* Plot the Inertia Values and Find the Elbow
* Check the Number of Customers in each Cluster
* Create a Heat Map of the Cluster Centers and Interpret the Clusters
* Update the Model Dataset
* Fit the Clustering Model with the Updated Data
* Create a DataFrame that combines the dataset, the "Exited" field, and cluster labels

### 📌 1. Data Preprocessing

* ✅ **Subset Selection:** Remove unnecessary fields (`CustomerId`, `Surname`, `Exited`)
* ✅ **Feature Engineering:** Create new features (e.g., `ProductsPerYear`)
* ✅ **Handling Categorical Data:** Convert `Gender`, `Geography` into numeric form
* ✅ **Data Scaling:** Use `StandardScaler` to standardize numeric fields

### 📌 2. Exploratory Data Analysis (EDA)

* ✅ **Distribution Analysis** & min/max value inspection
* ✅ **Correlation Analysis** to detect key relationships

### 📌 3. K-Means Clustering (Round 1)

* ✅ Apply Standardization
* ✅ Use Elbow Method for optimal k
* ✅ Fit Models and analyze inertia & silhouette scores
* ✅ Segment customers based on patterns

### 📌 4. K-Means Clustering (Round 2)

* ✅ Remove `Geography` to reduce bias
* ✅ Evaluate improved cluster relevance

### 📌 5. Insights & Business Recommendations

* ✅ Link clusters with churn rate
* ✅ Analyze country-specific trends
* ✅ Recommend strategies tailored to each segment

---

## 📈 Results & Key Findings

![image](https://github.com/user-attachments/assets/83357776-7339-4c76-abc6-ebafb3af4d60)

### 🔍 Identified Clusters

1. **Cluster 0:** Customers without credit cards
2. **Cluster 1:** High balance, few products, owns credit card
3. **Cluster 2:** Low balance, multiple products, owns credit card
4. **Cluster 3:** Recently acquired multiple products

### 🔥 Business Recommendations

* **Cluster 0:** Launch entry-level credit card; segment demographically
* **Cluster 1:** Offer investment products & advisory services
* **Cluster 2:** Reward loyalty with promotions and exclusive bundles
* **Cluster 3:** Offer long-term product retention incentives

---

## 🛠️ Technologies Used

* **Python** 🐍
* **Pandas & NumPy** (Data Processing)
* **Matplotlib & Seaborn** (Visualization)
* **Scikit-Learn** (Machine Learning & Clustering)

---
