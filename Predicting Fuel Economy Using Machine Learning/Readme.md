# 🚗 Predicting Fuel Economy: Regression-Based Models

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

## 📊 Dataset
The dataset (`auto-mpg.csv`) includes the following features:
- `mpg` (Target Variable)
- `weight`, `model_year`, `acceleration` (Predictor Variables)
- `origin` (Converted to a categorical variable)
- Other vehicle characteristics affecting fuel efficiency

---

## ⚙️ Methodology

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

### 🔍 Model Performance
| Model               | Test R² | Test MAE |
| ------------------- | ------- | -------- |
| Linear Regression  | 0.852   | 11.71    |
| Ridge Regression   | 0.818   | 9.372    |

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

## 📂 How to Use
1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Predicting-Fuel-Economy.git
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the Jupyter Notebook or Python script:
   ```bash
   jupyter notebook Predicting_Fuel_Economy.ipynb
   ```

---


---

### 🎯 This project showcases my expertise in data analysis, regression modeling, and feature engineering, making me a strong candidate for data analyst roles! 🚀


