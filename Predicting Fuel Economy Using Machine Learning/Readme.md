# 🚗 Predicting Fuel Economy: Regression-Based Models
![image](https://github.com/user-attachments/assets/9566f18e-5d59-4953-a914-573a8294c175)

## 📌 Overview
This project builds regression models to predict a vehicle's fuel efficiency (`mpg`) based on automobile characteristics such as weight, model year, acceleration, and more. It employs **Multiple Linear Regression** and **Ridge Regression** to analyze relationships and optimize predictions.

## 🎯 Objectives
1. **Prepare and Explore the Data**  
   - Handle missing values and format categorical variables.
   - Generate summary statistics and visualizations.
   
2. **Build a Multiple Regression Model**  
   - Identify the most correlated feature with `mpg`.
   - Fit a baseline and multiple regression model.
   
3. **Evaluate Model Performance & Interpret Results**  
   - Assess R² and MAE on the test dataset.
   - Perform residual analysis and check model assumptions.
   
4. **Compare with Ridge Regression**  
   - Implement Ridge Regression with cross-validation.
   - Compare performance with traditional regression.

---

## 📊 Dataset [Click Here to See Dataset](https://github.com/BI-with-Sabbir/Data-Driven-Decision-Making-Using-Python/blob/main/Predicting%20Fuel%20Economy%20Using%20Machine%20Learning/auto-mpg.csv)

![image](https://github.com/user-attachments/assets/c29dc169-b66e-4cca-8a74-fac26dbd0a7b)

The dataset (`auto-mpg.csv`) includes the following features:
- `mpg` (Target Variable)
- `weight`, `model_year`, `acceleration` (Predictor Variables)
- `origin` (Converted to a categorical variable)
- Other vehicle characteristics affecting fuel efficiency

---

## ⚙️ Methodology [Click Here to see My Python Notebook](https://github.com/BI-with-Sabbir/Data-Driven-Decision-Making-Using-Python/blob/main/Predicting%20Fuel%20Economy%20Using%20Machine%20Learning/Predicting%20Fuel%20Economy.ipynb)

### 📌 1. Data Preprocessing
✅ **Missing Values Handling:** Identify and address missing or inconsistent values.  
✅ **Feature Engineering:** Convert `origin` into a categorical feature.  
✅ **Visualization:** Create histograms and correlation heatmaps to analyze relationships.  

### 📌 2. Multiple Linear Regression
✅ **Feature Selection:** Identify the most correlated predictor for baseline modeling.  
✅ **Model Training:** Fit a multiple regression model using `statsmodels`.  
✅ **Validation Strategy:** Use **K-Fold Cross-Validation** to ensure model robustness.  

### 📌 3. Model Evaluation & Residual Analysis
✅ **Performance Metrics:** Report **R²** and **Mean Absolute Error (MAE)**.  
✅ **Residual Diagnostics:** Assess normality and homoscedasticity through scatterplots and Q-Q plots.  
✅ **Polynomial Feature Engineering:** Add squared terms to capture non-linearity.  

### 📌 4. Ridge Regression & Model Comparison
✅ **Standardization:** Scale features using `StandardScaler`.  
✅ **Cross-Validation:** Train Ridge Regression using **`RidgeCV`** with hyperparameter tuning.  
✅ **Performance Comparison:** Compare Ridge vs. Linear Regression in terms of R² and MAE.  

---

## 📈 Results & Key Findings

![image](https://github.com/user-attachments/assets/3fa3fd7a-a5a8-4b75-ba1b-97127b6fd24e)

### 🔍 Model Performance
| Model               | Test R² | Test MAE |
| ------------------- | ------- | -------- |
| Linear Regression  | 0.852   | 11.71    |
| Ridge Regression   | 0.818   | 9.372    |


![image](https://github.com/user-attachments/assets/892ac6e6-b944-479d-b0c8-1c564c6265c1)

### 🔥 Key Insights
- **Weight** is the most influential factor affecting fuel efficiency.
- The **Linear Model performed better than Ridge Regression**, indicating that regularization was unnecessary.
- **Polynomial terms** might further improve prediction accuracy.

---

## 🚀 Future Improvements
- **Polynomial Regression**: Introduce non-linear features for better predictions.
- **Lasso Regression**: Perform feature selection using L1 regularization.
- **Additional Data Sources**: Incorporate more features like fuel type and engine size.

---

## 🛠️ Technologies Used
- **Python** 🐍
- **Pandas & NumPy** (Data Processing)
- **Matplotlib & Seaborn** (Data Visualization)
- **Scikit-Learn** (Machine Learning Models)
- **Statsmodels** (Statistical Modeling)

---



