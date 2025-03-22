# Hourly Time Series Forecasting using XGBoost

## 📌 Project Overview
This project focuses on forecasting hourly energy consumption using XGBoost, a powerful gradient boosting algorithm. The dataset used comes from **PJM Interconnection LLC**, which operates an electric transmission system in the United States. The goal is to build an accurate time series model and extract valuable business insights from the predictions.

---

## 📊 Dataset Overview
- **Source:** PJM Hourly Energy Consumption Data
- **Time Period:** Covers multiple years with hourly electricity consumption data.
- **Region:** Data collected from PJM’s service areas across several U.S. states.
- **Target Variable:** Power consumption in megawatts (MW).
- **Features:** Timestamp, Hour, Day, Month, Year, and other time-related features.

---

## 🎯 Project Goal
The main objective is to develop a **time series forecasting model** using **XGBoost**, aiming to:
- Predict hourly power consumption.
- Identify key features influencing energy demand.
- Analyze forecast accuracy and areas for improvement.
- Extract business insights for power grid management.

---

## 🛠 Step-by-Step Work Process
### 1️⃣ **Data Preprocessing & Feature Engineering**
✔ Loaded and cleaned the dataset.
✔ Created time-based features: Hour, Day of Week, Month, Year, etc.
✔ Split the dataset into training (before 2015) and testing (after 2015).
✔ Handled missing values and ensured data consistency.

### 2️⃣ **Modeling with XGBoost**
✔ Implemented XGBoost for time series forecasting.
✔ Trained the model on historical data.
✔ Evaluated feature importance (Day of Year, Hour, and Year most significant).
✔ Generated predictions for unseen data.

### 3️⃣ **Performance Evaluation**
✔ **RMSE (Root Mean Squared Error):** 2,603,992.46  
✔ **MAE (Mean Absolute Error):** 1,237.15  
✔ **MAPE (Mean Absolute Percentage Error):** 8.26%  
✔ Analyzed best/worst predicted days.

### 4️⃣ **Insights from Forecast Errors**
✔ Model struggles with holidays (July 4th, Christmas, etc.).
✔ Over-forecasting on special days with abnormal consumption patterns.
✔ Need for additional external factors like weather data.

---

## 📈 Output Analysis
- The model effectively captures trends but faces challenges with special events.
- Feature importance analysis shows that **day of year, hour, and year** play the biggest roles in energy demand.
- Predicted values align with real-world consumption trends but require enhancements.

---

## 🔍 Business Impact & Insights
✔ **Improved Energy Planning:** Forecasting helps optimize power distribution.
✔ **Cost Reduction:** Predicting demand fluctuations can prevent overproduction.
✔ **Grid Stability:** Identifying peak hours prevents outages and improves efficiency.
✔ **Strategic Decision-Making:** Insights help policymakers manage energy supply.

---

## 🚀 Future Implementation
🔹 **Add Lag Variables:** Introduce past consumption data as new features.  
🔹 **Holiday Indicators:** Improve accuracy for special event days.  
🔹 **Weather Data Integration:** Consider temperature and humidity impact.  
🔹 **Hyperparameter Tuning:** Optimize XGBoost parameters for better performance.  

---

## ✅ Benefits of the Project
✔ Enhances forecasting accuracy for power grid operators.  
✔ Supports smart energy consumption and cost management.  
✔ Can be expanded to other industries like finance and retail.  
✔ Provides a scalable model for real-world deployment.  

---

## 📂 Repository Structure
```
📁 project-folder
 ┣ 📂 data  # Raw and processed datasets
 ┣ 📂 notebooks  # Jupyter notebooks for analysis
 ┣ 📂 models  # Trained models and saved outputs
 ┣ 📜 README.md  # Project documentation
 ┣ 📜 requirements.txt  # Dependencies list
 ┗ 📜 main.py  # Main script to run the model
```

---

## 💡 Conclusion
This project demonstrates how **XGBoost** can be used for **time series forecasting** in the energy sector. With further enhancements, the model can be a valuable tool for **energy demand prediction, cost reduction, and smart grid management.**



