**## A/B Testing in Python: SEO/Digital Marketing Campaign Analysis**

## **Project Overview**
A/B testing is a statistical method used to compare two different groups and determine whether there is a significant difference between them. In this project, we analyze the performance metrics of two different SEO/Digital Marketing campaigns to identify which strategy is more effective.

## **Project Goal**
The goal of this project is to evaluate the effectiveness of two different marketing campaigns (Group A and Group B) based on four key performance indicators (KPIs):
- **Impression**: Number of times the advertisement was viewed.
- **Click**: Number of times the advertisement was clicked.
- **Purchase**: Number of purchases made as a result of the campaign.
- **Earning**: Total revenue generated from purchases.

Using statistical hypothesis testing, we aim to determine if the differences in these metrics between the two campaigns are statistically significant.

## **Implementation Steps**
The following steps outline the methodology used to perform A/B testing:

### **Step 1: Importing the Dataset**
- The dataset consists of two groups stored in separate sheets of an Excel file.
- The data is loaded using `pandas.read_excel()`.

### **Step 2: Data Preprocessing & Feature Engineering**
- A new feature, **Earning per Purchase**, is created to measure the revenue efficiency per purchase.
- A **Group** column is added to differentiate Group A and Group B.

### **Step 3: Exploratory Data Analysis (EDA)**
- Summary statistics for each metric are calculated.
- Histograms and box plots are used to visualize the distribution of data.

### **Step 4: Testing the Normality Assumption**
- **Shapiro-Wilk Test** is performed to check if the data follows a normal distribution.
- If p-value > 0.05, the normality assumption holds; otherwise, non-parametric testing is required.

### **Step 5: Testing the Homogeneity of Variance**
- If normality holds, **Levene’s Test** is used to check if variances are equal between groups.
- If p-value > 0.05, equal variance is assumed; otherwise, Welch’s t-test is used.

### **Step 6: Hypothesis Testing**
#### **Case 1: Normal Distribution (Independent Samples t-Test)**
- If normality is confirmed, an **Independent Samples t-Test** is used to compare the means of Group A and Group B.
- If p-value < 0.05, we reject the null hypothesis and conclude a significant difference.

#### **Case 2: Non-Normal Distribution (Mann-Whitney U Test)**
- If the normality assumption is not met, the **Mann-Whitney U Test** is used as a non-parametric alternative.
- If p-value < 0.05, it indicates a significant difference in distributions.

## **Results & Interpretation**
- The **Shapiro-Wilk Test** showed that the data is **not normally distributed** (p < 0.05).
- As a result, the **Mann-Whitney U Test** was performed.
- The results showed a **statistically significant difference** (p < 0.05) in conversion rates between Group A and Group B.
- **Group B had a higher median conversion rate** compared to Group A, indicating a more effective campaign.

## **Real-World Applications**
A/B testing is widely used in various domains to optimize business decisions. Some real-world applications include:

1. **Digital Marketing Optimization**: Companies use A/B testing to compare different ad creatives, landing pages, or email marketing strategies to determine the most effective approach.
2. **E-commerce Performance Analysis**: Online retailers test different pricing strategies, product placements, or checkout processes to increase sales.
3. **User Experience (UX) Improvement**: Websites and mobile apps test different UI/UX designs to enhance user engagement.
4. **Pharmaceutical Trials**: In medical research, A/B testing helps compare the effectiveness of different treatments.

### **Example: A/B Testing in E-Commerce**
Consider an online store running two different advertisement campaigns:
- **Group A**: Uses a standard discount-based marketing approach.
- **Group B**: Uses personalized recommendations and dynamic pricing.

Through A/B testing, the company can determine which strategy leads to higher purchases and earnings, allowing for data-driven marketing decisions.

## **Conclusion**
This project successfully demonstrated the statistical steps required for A/B testing in Python. By applying hypothesis testing techniques, we identified a significant difference between two marketing strategies, allowing for evidence-based decision-making.

This analysis provides valuable insights for businesses looking to optimize their marketing campaigns and improve conversion rates using data-driven approaches.


