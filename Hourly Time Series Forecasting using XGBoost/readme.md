# Hourly Time Series Forecasting using XGBoost

## 📌 Table of Contents

* [Project Overview](#project-overview)
* [Dataset Overview](#dataset-overview)
* [Project Goal](#project-goal)
* [Step-by-Step Work Process](#step-by-step-work-process)
* [Output Analysis](#output-analysis)
* [Business Impact & Insights](#business-impact--insights)
* [Future Implementation](#future-implementation)
* [Repository Structure](#repository-structure)
* [Conclusion](#conclusion)

---

## 📌 Project Overview

This project focuses on forecasting hourly energy consumption using XGBoost, a powerful gradient boosting algorithm. The dataset used comes from **PJM Interconnection LLC**, which operates an electric transmission system in the United States. The goal is to build an accurate time series model and extract valuable business insights from the predictions.

![Energy Forecasting](https://github.com/user-attachments/assets/1b5c65c7-3dc5-43e2-9d8b-c1309d07ef6a)

---

## 📊 Dataset Overview

[Click here to download dataset](https://github.com/BI-with-Sabbir/Data-Driven-Decision-Making-Using-Python/blob/main/Hourly%20Time%20Series%20Forecasting%20using%20XGBoost/AEP_hourly.csv)

* **Source:** PJM Hourly Energy Consumption Data
* **Time Period:** Covers multiple years with hourly electricity consumption data.
* **Region:** Data collected from PJM’s service areas across several U.S. states.
* **Target Variable:** Power consumption in megawatts (MW).
* **Features:** Timestamp, Hour, Day, Month, Year, and other time-related features.

![Dataset Overview](https://github.com/user-attachments/assets/1459f90c-1a0c-4473-8e9a-1207a3abb73f)

---

## 🎯 Project Goal

The main objective is to develop a **time series forecasting model** using **XGBoost**, aiming to:

* Predict hourly power consumption.
* Identify key features influencing energy demand.
* Analyze forecast accuracy and areas for improvement.
* Extract business insights for power grid management.

---

## 🛠 Step-by-Step Work Process

[Click here to Open Python Notebook](https://github.com/BI-with-Sabbir/Data-Driven-Decision-Making-Using-Python/blob/main/Hourly%20Time%20Series%20Forecasting%20using%20XGBoost/Time_Series_Forecasting_with_XGBoost.ipynb)

### 1. Data Preprocessing & Feature Engineering

* Loaded and cleaned the dataset.
* Created time-based features: Hour, Day of Week, Month, Year, etc.
* Split the dataset into training (before 2015) and testing (after 2015).
* Handled missing values and ensured data consistency.

![Data Cleaning](https://github.com/user-attachments/assets/7ae1ccb0-8e7a-4de4-a4e6-f7588d30c9e5)

### 2. Modeling with XGBoost

* Implemented XGBoost for time series forecasting.
* Trained the model on historical data.
* Evaluated feature importance (Day of Year, Hour, and Year most significant).
* Generated predictions for unseen data.

![Modeling](https://github.com/user-attachments/assets/a529c352-b0a9-4b93-825c-9ec8a2d2c2e8)

### 3. Performance Evaluation

* **RMSE:** 2,603,992.46
* **MAE:** 1,237.15
* **MAPE:** 8.26%
* Analyzed best/worst predicted days.

### 4. Insights from Forecast Errors

* Model struggles with holidays (e.g., July 4th, Christmas).
* Over-forecasting on special days with abnormal consumption patterns.
* Need for additional external factors like weather data.

![Forecast Error](https://github.com/user-attachments/assets/7d9501f8-7d05-4d07-b1c1-315e9d6044ed)

---

## 📈 Output Analysis

* The model effectively captures trends but faces challenges with special events.
* Feature importance shows Day of Year, Hour, and Year as key influencers.
* Predictions align with real-world trends, though refinement is needed.

![Prediction Accuracy](https://github.com/user-attachments/assets/4c55dc9d-26b0-43d7-95d7-22be5179e6ea)

---

## 🔍 Business Impact & Insights

* **Improved Energy Planning:** Forecasting aids power distribution.
* **Cost Reduction:** Prevents overproduction with demand prediction.
* **Grid Stability:** Helps avoid outages and improves efficiency.
* **Strategic Decision-Making:** Enables smarter energy supply planning.

---

## 🚀 Future Implementation

* Add **Lag Variables** for capturing time-based trends.
* Integrate **Holiday Indicators** for abnormal consumption behavior.
* Include **Weather Data** to improve accuracy.
* Apply **Hyperparameter Tuning** for optimized model performance.

---

## 📂 Repository Structure

```
📁 project-folder
 ┣ 📂 data               # Raw and processed datasets
 ┣ 📂 notebooks          # Jupyter notebooks
 ┣ 📂 models             # Trained model files
 ┣ 📜 README.md          # Project documentation
 ┣ 📜 requirements.txt   # List of dependencies
 ┗ 📜 main.py            # Main script
```

---

## 💡 Conclusion

This project demonstrates how **XGBoost** can be used for **time series forecasting** in the energy sector. With further enhancement, the model can assist in energy demand prediction, cost savings, and smart grid optimization.
