# Chi-Square Test of Independence: Does Packaging Uniqueness Influence Purchase Decisions?

## 1. Project Name
**Unpacking the Influence: Chi-Square Analysis on Packaging and Purchase Behavior**
![image](https://github.com/user-attachments/assets/179b7d02-c68a-4952-9f6a-e7c3bbf2cb4c)


## 2. Dataset Details:
![image](https://github.com/user-attachments/assets/14e62df0-08ae-4f73-ab77-96a4390430cd)

- **Source**: Survey conducted by a Dog Food Company
- **Respondents**: 523 customers
- **Features**:
  - `Respondent`: Unique ID for each participant
  - `Uniqueness`: Customer perception of the packaging (5 levels: Extremely unique to Not at all unique)
  - `Purchase Likelihood`: Likelihood of purchasing the product (5 levels: Extremely likely to Not at all likely)
- **Format**: [Excel file](https://github.com/BI-with-Sabbir/Statistics-for-Data-Science-using-python/blob/main/Chi-square%20Test%20of%20Independence/Case%201%20-%20Chi-square%20test%20of%20independence.xlsx)

## 3. Decision Making
This project aimed to determine whether customers' perception of new, heavier, and uniquely designed packaging influenced their likelihood of purchasing the dog food. Using a Chi-Square Test of Independence, we examined whether there was a statistically significant association between the packaging's perceived uniqueness and the consumers' purchase intent.
![image](https://github.com/user-attachments/assets/607e71fc-dec0-4cd1-ae5f-40447a64244b)

- **Null Hypothesis (H0)**: Uniqueness is not associated with purchase intent.
- **Alternative Hypothesis (H1)**: Uniqueness is associated with purchase intent.
- **Significance Level**: α = 0.05
- **Chi-square statistic**: 21.39
- **Degrees of freedom**: 16
- **p-value**: 0.1641

- [Python code & Result](https://github.com/BI-with-Sabbir/Statistics-for-Data-Science-using-python/blob/main/Chi-square%20Test%20of%20Independence/Case_1_Chi_Square_Test_of_Independence.ipynb)

**Conclusion**: Since the p-value is greater than 0.05, we fail to reject the null hypothesis. There is no statistically significant association between the uniqueness of packaging and purchase likelihood.
![image](https://github.com/user-attachments/assets/e03833af-12ca-4450-b08b-e00a993f06df)


## 4. Why Use This for Business?
Businesses often make visual and structural changes to their packaging, assuming it will positively affect customer behavior. However, without data-driven validation, such decisions could lead to increased costs in logistics and materials without boosting sales. This project shows how businesses can use statistical tests like Chi-Square to validate marketing and product decisions before full-scale rollout.

## 5. Business Insight
- **Customer Perception**: While a segment of customers perceived the new packaging as highly unique, it didn’t translate into a significant increase in purchase intent.
- **Design vs. Decision**: Not all design changes lead to buying behavior changes. Investment in new packaging should consider actual impact on sales.
- **Strategic Focus**: The company might need to explore other factors influencing purchase behavior, such as pricing, product quality, or branding.
![image](https://github.com/user-attachments/assets/e71d0750-2a6e-4d96-985c-6d7e926da7b3)

## 6. Project Impact
- Helped the product and marketing teams avoid unnecessary packaging changes that wouldn't contribute to sales.
- Provided a framework for running similar hypothesis tests in future marketing experiments.
- Demonstrated how statistical thinking can lead to cost savings and more effective strategic decisions.

---

### 📊 Tools & Libraries Used
- Python (Pandas, NumPy, Matplotlib, SciPy)
- Excel for initial data collection
- Chi-Square Test of Independence

### 📁 Repository Structure
```
chi_square_packaging_analysis/
|-- data/
|   |-- Case 1 - Chi-square test of independence.xlsx
|-- src/
|   |-- analysis.ipynb
|-- visuals/
|   |-- contingency_table_plot.png
|-- README.md
```

### 🔗 Use Cases
- For Marketing Analysts exploring A/B test designs
- For Product Managers making data-informed packaging decisions
- For Data Analysts showcasing real-world hypothesis testing

---

### ✅ Result Summary
The new packaging design, despite being visually appreciated, does not have a statistically significant effect on consumer purchase likelihood based on the Chi-square test. Businesses should proceed cautiously when changing product design without empirical evidence of its influence on consumer behavior.



