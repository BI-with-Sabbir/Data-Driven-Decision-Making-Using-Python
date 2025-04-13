
# Python Fundamentals for Data Science: Advanced Essentials

Welcome to this beginner-to-intermediate level Python learning resource!  
This module builds upon Python basics and introduces **essential concepts** frequently used in **Data Science**, **Machine Learning**, and **real-world analytics workflows**.

---

## 📚 Table of Contents

- [🔹 Overview](#-overview)
- [✅ 1. List Comprehensions](#-1-list-comprehensions)
- [⚠️ 2. Error Handling (try, except)](#-2-error-handling-try-except)
- [📁 3. Working with Files](#-3-working-with-files)
- [⚡ 4. Lambda Functions](#-4-lambda-functions)
- [📚 5. Working with Libraries](#-5-working-with-libraries)
- [🧱 6. Introduction to Data Structures](#-6-introduction-to-data-structures)
- [🔄 7. Iterators and Generators](#-7-iterators-and-generators)
- [🏗️ 8. Introduction to Object-Oriented Programming (OOP)](#-8-introduction-to-object-oriented-programming-oop)
- [🧪 9. Practice Exercises](#-9-practice-exercises)
- [🚀 About This Module](#-about-this-module)

---

## 🔹 Overview

This session is designed to enhance your Python skills with topics critical for **data wrangling**, **ETL pipelines**, **custom modeling**, and **memory-efficient coding**.  
These concepts will make your Python code more Pythonic, modular, and scalable.

---

## ✅ 1. List Comprehensions

Concise syntax to **create**, **filter**, or **transform** lists.

```python
numbers = [1, 2, 3, 4, 5]
squares = [num ** 2 for num in numbers]
evens = [num for num in numbers if num % 2 == 0]
```

✅ Use Case: Compact transformation and filtering of data.

---

## ⚠️ 2. Error Handling (`try`, `except`)

Catch and manage exceptions to avoid crashing your program.

```python
try:
    num = int(input("Enter a number: "))
    print("You entered:", num)
except ValueError:
    print("Invalid input! Please enter a valid number.")
```

✅ Use Case: Missing or invalid user inputs, broken data files.

---

## 📁 3. Working with Files

Basic file I/O operations for text and dataset manipulation.

```python
# Writing to a file
with open("example.txt", "w") as file:
    file.write("Hello, World!")

# Reading the file
with open("example.txt", "r") as file:
    content = file.read()
    print(content)
```

✅ Use Case: Reading CSVs, writing logs, storing results.

---

## ⚡ 4. Lambda Functions

Anonymous functions for quick calculations and data transformations.

```python
double = lambda x: x * 2
doubled_list = list(map(lambda x: x * 2, [1, 2, 3, 4]))
```

✅ Use Case: Custom sorting, applying logic in `map()` or `filter()`.

---

## 📚 5. Working with Libraries

Importing built-in and third-party libraries.

```python
import math
import random

print(math.sqrt(16))
print(random.randint(1, 10))
```

✅ Use Case: Leverage modules for calculations, modeling, or visualization.

---

## 🧱 6. Introduction to Data Structures

Work with nested lists and dictionaries to manage complex data.

```python
# Nested List
matrix = [[1, 2], [3, 4]]

# Nested Dictionary
student = {
    "name": "Alice",
    "grades": {
        "math": 90,
        "science": 85
    }
}
```

✅ Use Case: Store tabular data, represent JSON-like structures.

---

## 🔄 7. Iterators and Generators

Generators yield items one at a time—great for memory efficiency.

```python
def generate_numbers(n):
    for i in range(n):
        yield i

for num in generate_numbers(5):
    print(num)
```

✅ Use Case: Streaming large files, building data pipelines.

---

## 🏗️ 8. Introduction to Object-Oriented Programming (OOP)

Classes and objects for reusable and structured code.

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, I’m {self.name} and I’m {self.age} years old.")

person = Person("Alice", 25)
person.greet()
```

✅ Use Case: Designing models, API classes, simulations.

---

## 🧪 9. Practice Exercises

- ✅ Use list comprehension to remove negative values from a list.
- ✅ Write a function to read a file and count the lines.
- ✅ Build a generator to yield Fibonacci numbers up to a given limit.
- ✅ Use a lambda function to sort a list of tuples by the second element.

---

## 🚀 About This Module

This content is part of a foundational Python series aimed at aspiring **Data Analysts**, **Data Scientists**, and **ML Engineers**.  
By the end of this module, you will be confident with advanced Python building blocks and ready to work with **Pandas**, **NumPy**, and other powerful data science libraries.

