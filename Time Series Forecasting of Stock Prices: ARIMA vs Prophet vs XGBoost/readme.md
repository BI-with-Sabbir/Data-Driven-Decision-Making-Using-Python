# 🏷️ Time Series Forecasting of Stock Prices: ARIMA vs Prophet vs XGBoost

<img width="1024" height="1024" alt="Wt_l3ZbVhmYpeEwNZdrKG" src="https://github.com/user-attachments/assets/7188fdf9-19d2-4888-835b-828334076f0b" />
<img width="1024" height="1024" alt="Wt_l3ZbVhmYpeEwNZdrKG" src="https://github.com/user-attachments/assets/7188fdf9-19d2-4888-835b-828334076f0b" />


---

## 📖 Table of Contents

* [📌 Project Overview](#-project-overview)
* [📊 Dataset Overview](#-dataset-overview)
* [🎯 Project Goal](#-project-goal)
* [🛠 Step-by-Step Work Process](#-step-by-step-work-process)
* [📈 Output Analysis](#-output-analysis)
* [🔍 Business Impact & Insights](#-business-impact--insights)
* [🚀 Future Implementation](#-future-implementation)
* [✅ Benefits of the Project](#-benefits-of-the-project)
* [📂 Repository Structure](#-repository-structure)
* [💡 Conclusion](#-conclusion)

---

## 📌 Project Overview

This project focuses on forecasting stock prices using three different time series forecasting approaches:

- **ARIMA** (Statistical Model)
- **Prophet** (Hybrid Forecasting Model)
- **XGBoost** (Machine Learning Model)

The project uses **Google (GOOGL) daily stock price data** over the last 10 years and compares the forecasting performance of these models. The aim is to identify which approach performs best for stock price prediction and to interpret the strengths and limitations of each method.

---

## 📊 Dataset Overview

* **Dataset:** Google (Alphabet Inc. - GOOGL) Daily Stock Prices
* **Source:** Yahoo Finance (`yfinance`)
* **Time Period:** Last 10 years
* **Frequency:** Business day
* **Target Variable:** Closing Price
* **Models Compared:** ARIMA, Prophet, XGBoost

### Main Variables
- Date
- Open
- High
- Low
- Close
- Volume

---

## 🎯 Project Goal

The main objective of this project is to:

* Forecast stock prices using statistical and machine learning approaches.
* Compare model performance using evaluation metrics.
* Understand the effect of stationarity, lag features, and rolling forecasting.
* Identify the most effective approach for practical stock forecasting.

---

## 🛠 Step-by-Step Work Process

### 1️⃣ Data Collection & Preprocessing

✔ Downloaded 10 years of Google stock price data using `yfinance`  
✔ Selected the **Close** price as the target variable  
✔ Converted the dataset to business-day frequency  
✔ Handled missing values using forward fill  

---

### 2️⃣ Exploratory Time Series Analysis

✔ Plotted historical stock price trends  
✔ Visualized the last 30 days of stock movement  
✔ Calculated **SMA** and **EMA** for trend smoothing  
✔ Applied **Exponential Smoothing**  
✔ Performed **Seasonal Decomposition** to examine trend, seasonality, and residuals  

---

### 3️⃣ Stationarity Check

✔ Conducted the **Augmented Dickey-Fuller (ADF) Test**  
✔ Confirmed that the raw closing price series was **non-stationary**  
✔ Applied first differencing to make the series more suitable for ARIMA modeling  

---

### 4️⃣ ARIMA Modeling

✔ Used **ACF** and **PACF** plots for parameter understanding  
✔ Applied **Auto-ARIMA** to find the best `(p,d,q)` order  
✔ Built a baseline ARIMA forecast  
✔ Improved performance using **walk-forward / rolling forecasting**  

**Key Insight:**  
Standard long-horizon ARIMA forecasting performed poorly, but rolling ARIMA improved significantly.

---

### 5️⃣ Prophet Modeling

✔ Prepared data using Prophet’s required column names: `ds` and `y`  
✔ Built a baseline Prophet model  
✔ Tuned Prophet parameters  
✔ Added lag-based regressor for improved forecasting  

**Key Insight:**  
Basic Prophet struggled with stock price dynamics, but lag-enhanced Prophet performed much better.

---

### 6️⃣ XGBoost Modeling

✔ Converted time series into a supervised learning problem  
✔ Created lag features and time-based features  
✔ Built a baseline XGBoost model  
✔ Improved the model using:
- lagged returns
- moving averages
- volatility
- RSI-like engineered indicators

**Key Insight:**  
XGBoost performed best when forecasting **returns** instead of raw stock prices.

---

### 7️⃣ Performance Evaluation

Models were compared using:

* **RMSE** – Root Mean Squared Error
* **MAE** – Mean Absolute Error

### Final Comparison Summary

| Model | Forecasting Strategy | RMSE | Performance |
|------|----------------------|------|-------------|
| ARIMA | Rolling Forecast | 4.16 | Strong |
| Prophet | Tuned / Lag Enhanced | 15.83 | Moderate |
| XGBoost | Return-Based Forecasting | 3.64 | Best |

---

## 📈 Output Analysis
# 1.Google Stoke price analysis last 10 years 
<img width="1395" height="588" alt="image" src="https://github.com/user-attachments/assets/0951e8a7-6bdc-4cc5-bb25-27125a0a3090" />
<img width="1395" height="588" alt="image" src="https://github.com/user-attachments/assets/0951e8a7-6bdc-4cc5-bb25-27125a0a3090" />

*interpret:
The 10-year GOOGL stock price shows a strong upward trend with increasing volatility over time. The series is clearly non-stationary, making direct long-horizon forecasting challenging. Structural changes, including rapid growth phases and market corrections, indicate that the underlying data-generating process evolves over time.

This behavior highlights the importance of:
- transforming the data (e.g., differencing or returns),
- using rolling forecasting strategies,
- and applying models capable of capturing nonlinear patterns.

Overall, the data suggests that short-term adaptive models are more suitable than static long-horizon approaches.

# 2. Moving Averages (SMA vs EMA)
<img width="1366" height="560" alt="image" src="https://github.com/user-attachments/assets/b7deee1d-2329-4201-b4fd-ac228d84fc4c" />
<img width="1366" height="560" alt="image" src="https://github.com/user-attachments/assets/b7deee1d-2329-4201-b4fd-ac228d84fc4c" />

### Interprtation 

![SMA vs EMA](outputs/figures/03_sma_ema.png)

**What the chart shows:**  
This plot compares the original stock price with 50-day Simple Moving Average (SMA) and Exponential Moving Average (EMA). Both indicators smooth the series and highlight the underlying trend.

**Why it matters:**  
EMA reacts faster to recent price changes, while SMA provides a more stable long-term trend. The lag in SMA during rapid price movements highlights its limitation in capturing short-term dynamics.

**Key takeaway:**  
The strong alignment of moving averages with the upward trend confirms market momentum, while the increasing deviation between price and averages suggests rising volatility—making adaptive forecasting models more suitable.

# 3. ### Exponential Smoothing (Holt Linear Trend)

![Holt Trend](outputs/figures/04_holt_trend.png)

**What the chart shows:**  
This plot compares actual stock prices with Holt’s Linear Trend, which applies exponential smoothing to capture the underlying trend.

**Why it matters:**  
The model closely follows the general upward movement while filtering out short-term noise. However, it lags during rapid price changes, indicating limited responsiveness to sudden market shifts.

**Key takeaway:**  
Stock prices are strongly trend-driven, but simple trend-based models are not sufficient for accurate forecasting due to high volatility and dynamic market behavior.

### Key Findings

* The raw stock price series showed a **strong upward trend** over time.
* The series was **non-stationary**, making raw price forecasting difficult.
* ARIMA performed poorly in direct long-horizon forecasting but improved greatly with rolling prediction.
* Prophet struggled because stock data contains weak seasonality and strong volatility.
* XGBoost achieved the best results after feature engineering and return-based forecasting.

---

## 🔍 Business Impact & Insights

✔ **Improved Forecast Understanding:** Shows how different forecasting approaches behave on financial time series.  
✔ **Model Comparison:** Helps analysts choose the right method for stock forecasting projects.  
✔ **Practical Learning:** Demonstrates why evaluation design and feature engineering matter more than simply choosing a model.  
✔ **Portfolio Value:** Strong end-to-end project combining statistics, machine learning, and financial analysis.  

---

## 🚀 Future Implementation

🔹 Add **LSTM / GRU** deep learning models for comparison  
🔹 Include **technical indicators** such as MACD and Bollinger Bands  
🔹 Add **sentiment analysis** from financial news  
🔹 Perform **cross-validation for time series**  
🔹 Deploy the best model using **Streamlit** or **Flask**  

---

## ✅ Benefits of the Project

✔ Demonstrates both **statistical** and **machine learning** forecasting methods  
✔ Useful for learning real-world time series forecasting workflows  
✔ Highlights challenges of stock price prediction  
✔ Provides a strong portfolio project for Data Analyst / BI / Data Science roles  

---

## 📂 Repository Structure

```bash
📁 time-series-forecasting-arima-prophet-xgboost
 ┣ 📂 data
 ┃ ┣ 📂 raw
 ┃ ┗ 📂 processed
 ┣ 📂 notebooks
 ┃ ┗ 📜 Time_Series_Forecasting_ARIMA_vs_Prophet_vs_XGBoost.ipynb
 ┣ 📂 outputs
 ┃ ┣ 📂 figures
 ┃ ┣ 📂 metrics
 ┃ ┗ 📂 forecasts
 ┣ 📂 src
 ┃ ┣ 📜 data_loader.py
 ┃ ┣ 📜 preprocessing.py
 ┃ ┣ 📜 arima_model.py
 ┃ ┣ 📜 prophet_model.py
 ┃ ┣ 📜 xgboost_model.py
 ┃ ┣ 📜 evaluation.py
 ┃ ┗ 📜 utils.py
 ┣ 📜 README.md
 ┣ 📜 requirements.txt
 ┣ 📜 .gitignore
 ┗ 📜 LICENSE
