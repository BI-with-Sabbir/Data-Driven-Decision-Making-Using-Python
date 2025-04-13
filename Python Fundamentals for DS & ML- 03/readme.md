# 🐍 Python Basics: Conditional Statements, Functions & Loops

Welcome to this beginner-friendly Python learning resource!  
This session is specially designed to introduce **Conditional Statements**, **User-Defined Functions**, and **Iterations** through **practical examples** and **real-life use cases**.

---

## 📚 Table of Contents

- [🔹 Session Outline](#-session-outline)
- [✅ 1. Conditional Statements: if, elif, else](#-1-conditional-statements-if-elif-else)
- [🛠 2. User-Defined Functions](#-2-user-defined-functions)
- [🧩 3. Functions with Parameters](#-3-functions-with-parameters)
- [🔄 4. Function Within a Function](#-4-function-within-a-function)
- [🧠 5. Combining Conditions and Functions](#-5-combining-conditions-and-functions)
- [🔁 6. Iteration: for and while Loops](#-6-iteration-for-and-while-loops)
- [🧪 7. Combining Conditions and Loops](#-7-combining-conditions-and-loops)
- [⚙️ 8. Combining Conditions, Functions, and Loops](#-8-combining-conditions-functions-and-loops)
- [📦 9. Iterating Over Dictionaries](#-9-iterating-over-dictionaries)
- [📝 10. Practice Exercises](#-10-practice-exercises)

---

## 🔹 Session Outline

- IF & ELIF Statements
- Creating Functions in Python
- Parameters and Arguments
- Nested Functions
- Combining Conditions and Functions
- For & While Loops
- Iteration over Dictionaries
- Hands-on Practice Exercises

---

## ✅ 1. Conditional Statements: `if`, `elif`, `else`

Used to control the flow of your program based on logic.

```python
age = 18

if age < 13:
    print("You are a child.")
elif age < 20:
    print("You are a teenager.")
else:
    print("You are an adult.")

📌 Use Case: Age-based categorization or validation of user input.

.

🛠 2. User-Defined Functions
Functions are reusable blocks of code that perform a specific task.

```python
def greet():
    print("Hello, World!")

greet()

📌 Use Case: Reusing code for repetitive tasks.

🧩 3. Functions with Parameters
Passing values to a function for more flexibility.

```python
def greet_user(name):
    print(f"Hello, {name}!")

greet_user("Alice")

Example: Palindrome Checker

```python
def isPalindrome(s):
    return s == s[::-1]

s = "malayalam"
print("Yes" if isPalindrome(s) else "No")

📌 Use Case: Personalizing output, string or data processing.


🔄 4. Function Within a Function
Organize code better by nesting functions.

```python
def outer_function():
    print("This is the outer function.")
    def inner_function():
        print("This is the inner function.")
    inner_function()

outer_function()

📌 Use Case: Modularizing large tasks.


🧠 5. Combining Conditions and Functions

```python
def check_even_odd(number):
    if number % 2 == 0:
        print(f"{number} is even.")
    else:
        print(f"{number} is odd.")

check_even_odd(10)
check_even_odd(7)

📌 Use Case: Conditional validation inside reusable functions.

🔁 6. Iteration: for and while Loops

```python
# for loop
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# while loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

📌 Use Case: Repeating tasks until a condition is met.

🧪 7. Combining Conditions and Loops

```python
numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num % 2 == 0:
        print(f"{num} is even.")
    else:
        print(f"{num} is odd.")
📌 Use Case: Looping through datasets and applying logic.

⚙️ 8. Combining Conditions, Functions, and Loops

```python
def print_squares(numbers):
    for num in numbers:
        print(f"Square of {num} is {num ** 2}.")

numbers = [1, 2, 3, 4, 5]
print_squares(numbers)

📌 Use Case: Transforming and analyzing data.

📦 9. Iterating Over Dictionaries

```python
person = {
    "name": "Alice",
    "age": 25,
    "is_student": True
}

# keys and values
for key, value in person.items():
    print(f"{key}: {value}")

# keys
for key in person.keys():
    print("Key:", key)

# values
for value in person.values():
    print("Value:", value)

📌 Use Case: Looping through structured data (e.g., JSON, configs).

📝 10. Practice Exercises
✅ 1. Sum of Even Numbers


```python
def sum_even(numbers):
    return sum(num for num in numbers if num % 2 == 0)
✅ 2. While Loop for User Input


```python
while True:
    user_input = input("Enter something (type 'quit' to exit): ")
    if user_input.lower() == "quit":
        break
✅ 3. Average Grade Calculator


```python
grades = {"Alice": 85, "Bob": 90, "Charlie": 78}

def average_grade(grades_dict):
    return sum(grades_dict.values()) / len(grades_dict)

print("Average Grade:", average_grade(grades))

🚀 About This Module
This learning module is ideal for:

🧑‍🎓 Absolute beginners in Python

💼 Aspiring data analysts and developers

🧪 Learners who prefer real-life examples

Designed & maintained by [Sabbir Hossain Rossi]

📌 Follow me on GitHub for more learning resources and projects!


