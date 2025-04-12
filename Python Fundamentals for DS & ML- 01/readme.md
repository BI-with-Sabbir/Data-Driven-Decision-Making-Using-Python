# Python Fundamentals for Data Science & Machine Learning

This Jupyter Notebook provides a beginner-friendly introduction to Python programming, tailored specifically for those pursuing careers in **Data Science** and **Machine Learning**.

---

## 📘 Session Overview

This is the first notebook in a foundational series aimed at building core Python skills necessary for data analysis, machine learning, and statistical computing. [click here](https://github.com/BI-with-Sabbir/Data-Driven-Decision-Making-Using-Python/blob/main/Python%20Fundamentals%20for%20DS%20%26%20ML-%2001/Python%20Fundamentals%20for%20DS%20%26%20ML-%2001%20(1).pdf)

### 🧠 Topics Covered

- ✅ Introduction to Python
- ✅ Introduction to Google Colab & Jupyter Notebook
- ✅ Getting familiar with the Notebook Interface
- ✅ Python Data Types:
  - Numeric (int, float)
  - Strings
  - Boolean
  - List, Tuple
  - Dictionary, Set
  - NoneType
- ✅ Concept of Mutability: List vs Tuple
- ✅ Conditional Statements
- ✅ Basic Input & Output Operations

---

## 🧪 Sample Code Snippets

```python
# Numeric Types
age = 25
height = 5.9
print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))

# String Concatenation
name = "Rossi"
greeting = 'Hello, ' + name
print(greeting)

# Boolean and Conditional
is_student = True
if is_student:
    print("Student detected!")

# Example: Lists

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add an item using the "append" Method
print("Fruits:", fruits)
print("First fruit:", fruits[1])  # Access by index

# Example: Tuples

coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)
print("X-coordinate:", coordinates[0])

# prompt: Create a dictionary with Keys: Customer Name, Number of Items Purchased, Age
# Add Multiple values under each key

customer_data = {
    'Customer Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Number of Items Purchased': [5, 2, 8, 3],
    'Age': [25, 30, 22, 40]
}

# prompt: Convert the customer_data list as dataframe

import pandas as pd

customer_data = {
    'Customer Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Number of Items Purchased': [5, 2, 8, 3],
    'Age': [25, 30, 22, 40]
}

customer_df = pd.DataFrame(customer_data)
customer_df

# Example: Dictionaries

person = {"name": "Nayeem",
          "age": 25,
          "is_student": True}
print("Person:", person)
print("Name:", person["name"])  # Access by key
person["age"] = 26  # Update value
print("Person:", person)
```

---

### Dictionaries Methode:
![image](https://github.com/user-attachments/assets/98972532-4507-4e64-85f0-4e8c0f382e79)

### Nested Dictionaries Method:
![image](https://github.com/user-attachments/assets/8c524a76-f463-4a0d-823f-4d8bd49f65c7)

### Set operations:
![image](https://github.com/user-attachments/assets/8b6835a4-c4a0-4e57-a7b9-a103fd36522e)

### List & Tuple 
![image](https://github.com/user-attachments/assets/075d3dfa-9d27-4bf9-87f8-43d9a4681f69)




## 📚 Prerequisites

- No prior coding experience required.
- Basic familiarity with using a web browser and typing code into a notebook environment.

---

## 🚀 Tools Used

- [Google Colab](https://colab.research.google.com/)
- Jupyter Notebook

---

## 📈 Who is this for?

- Students beginning their journey in **Data Science** or **Machine Learning**
- Aspiring Data Analysts
- Non-CS background learners looking to learn Python for data work

---

## 🛠️ Next Steps

In future notebooks, we’ll cover:
- Python for Data Analysis using `pandas` and `numpy`
- Data Visualization
- Exploratory Data Analysis (EDA)
- Machine Learning Algorithms with `scikit-learn`

