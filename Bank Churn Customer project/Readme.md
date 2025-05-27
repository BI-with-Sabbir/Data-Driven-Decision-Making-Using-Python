## Bank Churn Customer Analysis

## 📌 Project Overview
This project focuses on **data cleaning, exploratory data analysis (EDA), and machine learning classification** to predict customer churn for a bank. The goal is to analyze customer data, identify key patterns, and build predictive models to help the bank reduce churn and improve customer retention.

## 📂 Dataset Description
The dataset consists of customer information, including demographics, account details, and transaction history. Key features include:
- **Customer ID**: Unique identifier for each customer
- **Age, Gender, Geography**: Demographic details
- **Credit Score**: Financial stability indicator
- **Balance, Estimated Salary**: Financial behavior indicators
- **Tenure, Number of Products**: Customer relationship with the bank
- **Exited**: Target variable (1 = Churned, 0 = Retained)

## 🛠️ Data Cleaning & EDA
- **Handling Missing Values**: Checked and imputed missing values
- **Duplicate Removal**: Eliminated redundant records
- **Feature Engineering**: Created new features to improve predictive performance
- **Exploratory Data Analysis**: 
  - Distribution of key variables
  - Churn rate across different demographics
  - Correlation analysis between features

## 🔍 Machine Learning Models Used
Implemented classification models to predict customer churn:
- **Logistic Regression**
- **Random Forest Classifier**
- **XGBoost Classifier**

## 📊 Results & Insights
- Identified key factors influencing churn, such as credit score, tenure, and balance.
- Evaluated model performance using **accuracy, precision, recall, and F1-score**.
- Provided actionable insights to reduce churn and retain customers.


##📊 Key Insights for Decision-Making

Based on the analysis, the following insights are valuable for stakeholders:

📌 High Churn Rate among Younger Customers: Customers aged 18-30 have a significantly higher churn rate. The bank should introduce loyalty programs for younger customers.

📌 Geographic Influence on Churn: Customers from certain regions (e.g., Germany) show a higher churn rate. The bank should investigate region-specific policies or offers.

📌 Impact of Credit Score & Balance: Customers with low credit scores and high account balances tend to churn more. Offering personalized financial advice or incentives may reduce churn.

📌 Multi-Product Users Stay Longer: Customers with multiple products (loans, savings, etc.) have a lower churn rate. The bank should encourage bundling services.

📌 High Churn from Online Services: Customers primarily using online services exhibit higher churn. Improving digital banking experience and customer support may help.

## 🚀 Future Improvements
- Implement **Customer Segmentation (Unsupervised Learning)** using clustering techniques.
- Test **Deep Learning Models** (e.g., Neural Networks) for better prediction accuracy.
- Develop a **Web Dashboard** for interactive insights.
