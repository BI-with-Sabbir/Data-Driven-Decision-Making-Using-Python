# 🏷️ Time Series Forecasting of Stock Prices: ARIMA vs Prophet vs XGBoost

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


The 10-year GOOGL stock price shows a strong upward trend with increasing volatility over time. The series is clearly non-stationary, making direct long-horizon forecasting challenging. Structural changes, including rapid growth phases and market corrections, indicate that the underlying data-generating process evolves over time.

This behavior highlights the importance of:
- transforming the data (e.g., differencing or returns),
- using rolling forecasting strategies,
- and applying models capable of capturing nonlinear patterns.

Overall, the data suggests that short-term adaptive models are more suitable than static long-horizon approaches.

# 2. Moving Averages (SMA vs EMA)
<img width="1366" height="560" alt="image" src="https://github.com/user-attachments/assets/b7deee1d-2329-4201-b4fd-ac228d84fc4c" />


**What the chart shows:**  
This plot compares the original stock price with 50-day Simple Moving Average (SMA) and Exponential Moving Average (EMA). Both indicators smooth the series and highlight the underlying trend.

**Why it matters:**  
EMA reacts faster to recent price changes, while SMA provides a more stable long-term trend. The lag in SMA during rapid price movements highlights its limitation in capturing short-term dynamics.

**Key takeaway:**  
The strong alignment of moving averages with the upward trend confirms market momentum, while the increasing deviation between price and averages suggests rising volatility—making adaptive forecasting models more suitable.

# 3. Exponential Smoothing (Holt Linear Trend)

<img width="1404" height="560" alt="image" src="https://github.com/user-attachments/assets/f4ef484a-84e7-49e8-b7dc-bd709c3f2163" />

**What the chart shows:**  
This plot compares actual stock prices with Holt’s Linear Trend, which applies exponential smoothing to capture the underlying trend.

**Why it matters:**  
The model closely follows the general upward movement while filtering out short-term noise. However, it lags during rapid price changes, indicating limited responsiveness to sudden market shifts.

**Key takeaway:**  
Stock prices are strongly trend-driven, but simple trend-based models are not sufficient for accurate forecasting due to high volatility and dynamic market behavior.

# 4.Time Series Decomposition

<img width="1477" height="949" alt="image" src="https://github.com/user-attachments/assets/28df172f-68d2-453f-97c4-f9bd1e74c3eb" />

**What the chart shows:**  
The decomposition splits the stock price into trend, seasonal, and residual components. The trend shows strong long-term growth with a temporary decline around 2022–2023, followed by rapid acceleration.

**Why it matters:**  
The seasonal component is relatively weak, indicating that stock prices do not follow strong periodic patterns. The residual component shows increasing volatility over time, reflecting market uncertainty and external influences.

# 5. ARIMA Forecast vs Actual
<img width="1366" height="560" alt="image" src="https://github.com/user-attachments/assets/61a6aa27-c920-4b9f-96da-2fd52651bd47" />

**What the chart shows:**  
The ARIMA model produces a relatively smooth forecast that fails to capture the sharp fluctuations and rapid growth observed in the actual stock price.

**Why it matters:**  
The model underestimates volatility and trend acceleration, indicating limitations in handling non-stationary and highly dynamic financial time series.

**Key takeaway:**  
Standard ARIMA is not suitable for long-horizon stock forecasting without adaptive updating strategies such as rolling forecasts.

# 6. ARIMA Walk-Forward Forecast
<img width="1390" height="560" alt="image" src="https://github.com/user-attachments/assets/0ef61689-73ed-4a96-93ce-cd7f7f728e3d" />

**What the chart shows:**  
The ARIMA rolling forecast closely follows the actual stock price, capturing both short-term fluctuations and overall trend.

**Why it matters:**  
Unlike static forecasting, the walk-forward approach updates the model continuously, allowing it to adapt to new data and changing market conditions.

**Key takeaway:**  
ARIMA performs significantly better when applied in a rolling forecasting framework, making it a strong baseline for short-term stock prediction.

# 7. XGBoost Forecast (Raw Price)

<img width="1391" height="560" alt="image" src="https://github.com/user-attachments/assets/bdb1c864-ad50-441d-a9fe-ea4af306550f" />

**What the chart shows:**  
The XGBoost model captures short-term fluctuations but fails to follow the strong upward trend in the stock price.

**Why it matters:**  
Tree-based models like XGBoost are not well-suited for extrapolating beyond the range of training data when predicting non-stationary time series such as raw stock prices.

**Key takeaway:**  
Predicting raw prices with machine learning is ineffective; transforming the problem (e.g., predicting returns) is essential for improved performance.

**Key takeaway:**  
The series is trend-dominated with weak seasonality and high noise, making it more suitable for adaptive, short-term forecasting models rather than static seasonal approaches.

# 8. XGBoost Forecast (Corrected with Daily Updates)
<img width="1391" height="560" alt="image" src="https://github.com/user-attachments/assets/63e19bc2-aa1d-498e-919d-41512afbfdb5" />

**What the chart shows:**  
The corrected XGBoost model closely tracks the actual stock price using a one-step-ahead prediction strategy with daily updates.

**Why it matters:**  
By avoiding long-horizon recursive forecasting and using updated real values at each step, the model eliminates error accumulation and captures both trend and short-term fluctuations effectively.
**Key takeaway:**  
Adaptive, one-step forecasting combined with proper feature engineering enables XGBoost to outperform traditional statistical models for stock prediction.

# 9. XGBoost 7-Day Future Forecast

<img width="960" height="507" alt="image" src="https://github.com/user-attachments/assets/9d17e416-05e3-4a49-8257-a0618d9e1eb1" />

**What the chart shows:**  
The model predicts a gradual decline in stock price over the next 7 days, starting from approximately 307.16.

**Why it matters:**  
This suggests a short-term correction following recent strong upward momentum, which is common in financial markets after rapid price increases.

**Key takeaway:**  
The forecast indicates a mild bearish trend in the short term, highlighting the importance of adaptive forecasting for short-horizon decision-making.

# 10. Prophet Forecast

<img width="1390" height="560" alt="image" src="https://github.com/user-attachments/assets/6861a767-9ade-4470-b81d-0d809cbb715e" />

**What the chart shows:**  
The Prophet model captures the overall upward trend in stock prices while smoothing out short-term fluctuations.

**Why it matters:**  
Although Prophet performs well in identifying long-term trends, it struggles to respond to sudden market movements and high volatility, which are common in financial time series.

**Key takeaway:**  
Prophet is better suited for trend-focused forecasting but requires additional features (e.g., lag variables) to improve performance in dynamic stock market environments.

# 11. Final Prophet Forecast (Corrected with Momentum)

<img width="1390" height="560" alt="image" src="https://github.com/user-attachments/assets/80406af1-3008-4be0-8474-c94f29696b66" />


**What the chart shows:**  
The improved Prophet model incorporates momentum (lag features) and better follows the actual stock price trend.

**Why it matters:**  
While the model becomes more responsive to recent changes, it also introduces higher variability and occasional overreaction to fluctuations.

**Key takeaway:**  
Enhancing Prophet improves directional accuracy but increases noise, making it less stable compared to rolling statistical models or machine learning approaches.


# 12. Prophet Components Analysis
    <img width="878" height="1478" alt="image" src="https://github.com/user-attachments/assets/93fd1ab1-b503-4324-96a8-023dbe01bc9e" />

**What the chart shows:**  
The Prophet model decomposes the time series into trend, seasonal, holiday, and extra regressor components.

**Why it matters:**  
The trend and momentum (extra regressor) dominate the model, while seasonal and holiday effects are minimal, indicating that stock prices are driven more by recent movements than by periodic patterns.

#13. Model Performance Comparison (MAE)

<img width="948" height="507" alt="image" src="https://github.com/user-attachments/assets/ee319fd3-0771-4658-a40b-b3a0407074c7" />

**What the chart shows:**  
The baseline comparison of ARIMA, Prophet, and XGBoost using MAE shows similar performance across all models, with Prophet and XGBoost slightly outperforming ARIMA.

**Why it matters:**  
The small performance gap indicates that model choice alone is not the primary driver of forecasting accuracy.

**Key takeaway:**  
Significant improvements were achieved only after refining forecasting strategies (rolling forecasts) and applying proper feature engineering, particularly for XGBoost.

**Key takeaway:**  
Feature engineering (momentum/lag variables) is critical for improving Prophet performance, as traditional seasonal components have limited predictive value in financial time series.
<img width="878" height="1478" alt="image" src="https://github.com/user-attachments/assets/805c400f-aee3-4e80-b7da-6cfd95af2b4e" />


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

