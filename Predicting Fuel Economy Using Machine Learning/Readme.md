# 🚗 Predicting Fuel Economy: Regression-Based Models

## 🔗 Context Navigation

Click to navigate to a section:

* [📌 Overview](#-overview)
* [🎯 Objectives](#-objectives)
* [📊 Dataset](#-dataset)
* [⚙️ Methodology](#️-methodology)
* [📈 Results & Key Findings](#-results--key-findings)
* [🔥 Key Insights](#-key-insights)
* [🚀 Future Improvements](#-future-improvements)
* [🛠️ Technologies Used](#-technologies-used)

---

## 📌 Overview

This project builds regression models to predict a vehicle's fuel efficiency (`mpg`) based on automobile characteristics such as weight, model year, acceleration, and more. It employs **Multiple Linear Regression** and **Ridge Regression** to analyze relationships and optimize predictions.

---

## 🎯 Objectives

1. **Prepare and Explore the Data**

   * Handle missing values and format categorical variables.
   * Generate summary statistics and visualizations.

2. **Build a Multiple Regression Model**

   * Identify the most correlated feature with `mpg`.
   * Fit a baseline and multiple regression model.

3. **Evaluate Model Performance & Interpret Results**

   * Assess R² and MAE on the test dataset.
   * Perform residual analysis and check model assumptions.

4. **Compare with Ridge Regression**

   * Implement Ridge Regression with cross-validation.
   * Compare performance with traditional regression.

---

## 📊 Dataset [Click Here to See Dataset](https://github.com/BI-with-Sabbir/Data-Driven-Decision-Making-Using-Python/blob/main/Predicting%20Fuel%20Economy%20Using%20Machine%20Learning/auto-mpg.csv)

The dataset (`auto-mpg.csv`) includes the following features:

* `mpg` (Target Variable)
* `weight`, `model_year`, `acceleration` (Predictor Variables)
* `origin` (Converted to a categorical variable)
* Other vehicle characteristics affecting fuel efficiency

---

## ⚙️ Methodology [Click Here to see My Python Notebook](https://github.com/BI-with-Sabbir/Data-Driven-Decision-Making-Using-Python/blob/main/Predicting%20Fuel%20Economy%20Using%20Machine%20Learning/Predicting%20Fuel%20Economy.ipynb)

### 📌 1. Data Preprocessing

* ✅ Missing Values Handling
* ✅ Feature Engineering
* ✅ Visualization with histograms and heatmaps

### 📌 2. Multiple Linear Regression

* ✅ Feature Selection
* ✅ Model Training using `statsmodels`
* ✅ K-Fold Cross-Validation

### 📌 3. Model Evaluation & Residual Analysis

* ✅ Performance Metrics (R², MAE)
* ✅ Residual Diagnostics (Q-Q plots, scatterplots)
* ✅ Polynomial Features

### 📌 4. Ridge Regression & Model Comparison

* ✅ Feature Scaling
* ✅ Hyperparameter Tuning with `RidgeCV`
* ✅ Model Performance Comparison

---

## 📈 Results & Key Findings

### 🔍 Model Performance

| Model             | Test R² | Test MAE |
| ----------------- | ------- | -------- |
| Linear Regression | 0.852   | 11.71    |
| Ridge Regression  | 0.818   | 9.372    |

---

## 🔥 Key Insights

* **Weight** is the most influential factor affecting fuel efficiency.
* **Linear Model performed better than Ridge Regression**, indicating that regularization was unnecessary.
* **Polynomial terms** could further improve accuracy.

---

## 🚀 Future Improvements

* Polynomial Regression for capturing non-linear relationships.
* Lasso Regression for automatic feature selection.
* Integrating features like fuel type, engine size, and transmission type.

---

## 🛠️ Technologies Used

* **Python** 🐍
* **Pandas & NumPy** (Data Processing)
* **Matplotlib & Seaborn** (Data Visualization)
* **Scikit-Learn** (Machine Learning Models)
* **Statsmodels** (Statistical Modeling)

---
