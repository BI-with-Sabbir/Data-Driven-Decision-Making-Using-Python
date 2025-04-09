#**Basics of Python Programming Language**

##**Outline:**

- Introduction to Python
- Introduction to Google Colab & Jupyter Notebook for Writing and
 Executing Python Codes.
- Getting used to the User Interface (UI) of Jupyter Notebook/Google Colab.
- Python Data Types: Numeric, Strings, Boolean, List, Dictionary, Tuple,
 Set, None.
- Iterables & Mutability; List vs. Tuples.

## **1. Introduction to Python:**

**What is Python?**

- Python is a high-level, interpreted, and general-purpose programming language.

- Known for its simplicity and readability, making it ideal for beginners.

- Widely used in Data Science, Machine Learning, Web Development, Automation, and more.

**Why Python for Data Science and Machine Learning?**

- Rich ecosystem of libraries (e.g., NumPy, Pandas, scipy, matplotlib, plotly, statsmodels, Scikit-learn, TensorFlow).

- Easy to learn and use, with a large community for support.

- Great for prototyping and production-level code.

## **2. Introduction to Google Colab & Jupyter Notebook**

**What are Google Colab and Jupyter Notebook?**

**Google Colab:** A free, cloud-based platform for writing and executing Python code in a notebook environment.

**Jupyter Notebook:** An open-source web application for creating and sharing documents with live code, equations, and visualizations.

**Why use them?**

* Interactive Coding Environment.

* Easy to Share and Collaboration.

* No Setup Required (especially for Google Colab).

**Getting Started with Google Colab:**

* Open [Google Colab](https://colab.research.google.com/).

* Create a new notebook.

* Familiarize yourself with the interface:

* Cells for code or text.

* Run cells using Shift + Enter.

* Add new cells using the + button.

## **3. Python Data Types**

Python has several built-in data types. Let’s explore them with examples:

**1. Numeric Types:**

* Integers (int): Whole numbers (e.g., 5, -3).


* Floats (float): Decimal numbers (e.g., 3.14, -0.001).


```python
# Example: Numeric Types
age = 25          # int
height = 5.9      # float
print("Age:", age, "Type:", type(age))
print("Height:", height, "Type:", type(height))
```

    Age: 25 Type: <class 'int'>
    Height: 5.9 Type: <class 'float'>
    

**Real-life Use Case:**

Storing age, height, temperature, or any measurable quantity.

**2. Strings (str):**

* A sequence of characters enclosed in single or double quotes.

* Strings are immutable (cannot be changed after creation).


```python
# Example: Strings

name = "Rossi"
greeting = 'Hello, ' + name
print(greeting)
print("Length of name:", len(name))
```

    Hello, Rossi
    Length of name: 5
    

**Real-life Use Case:**

Storing names, addresses, or text data.

**3. Boolean (bool):**

* Represents True or False.

* Used in conditions and logical operations.


```python
# Example: Boolean

is_student = True
is_working = False
print("Is student?", is_student)
print("Is working?", is_working)
```

    Is student? True
    Is working? False
    


```python
age = 18
if age > 60: #If Evaluated True then the first part will be printed.
    print("You are a senior citizen")
elif age > 18: #If Evaluated True then the second part will be printed.
    print("You are an adult")
else:
    print("You are not an adult")
```

    You are not an adult
    

**Real-life Use Case:**

Checking conditions (e.g., "Is the user logged in?").

**4. Lists (list):**

* Ordered, mutable collection of items.

* Can contain mixed data types.


```python
# Example: Lists

fruits = ["apple", "banana", "cherry"]
fruits.append("orange")  # Add an item using the "append" Method
print("Fruits:", fruits)
print("First fruit:", fruits[1])  # Access by index
```

    Fruits: ['apple', 'banana', 'cherry', 'orange']
    First fruit: banana
    

**NB:** Python is Zero Indexed; Starts from O

**Real-life Use Case:**

Storing a list of items, such as shopping lists or to-do tasks.

**5. Tuples (tuple):**

* Ordered, immutable collection of items.

* Faster than lists for fixed data.


```python
# Example: Tuples

coordinates = (10.0, 20.0)
print("Coordinates:", coordinates)
print("X-coordinate:", coordinates[0])
```

    Coordinates: (10.0, 20.0)
    X-coordinate: 10.0
    

**Real-life Use Case:**

Storing fixed data, such as coordinates or RGB values.

**6. Dictionaries (dict):**

* Unordered collection of key-value pairs.

* Keys must be unique and immutable.


```python
# prompt: Create a dictionary with Keys: Customer Name, Number of Items Purchased, Age
# Add Multiple values under each key

customer_data = {
    'Customer Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Number of Items Purchased': [5, 2, 8, 3],
    'Age': [25, 30, 22, 40]
}

```


```python
# prompt: Convert the customer_data list as dataframe

import pandas as pd

customer_data = {
    'Customer Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Number of Items Purchased': [5, 2, 8, 3],
    'Age': [25, 30, 22, 40]
}

customer_df = pd.DataFrame(customer_data)
customer_df

```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Customer Name</th>
      <th>Number of Items Purchased</th>
      <th>Age</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>5</td>
      <td>25</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Bob</td>
      <td>2</td>
      <td>30</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Charlie</td>
      <td>8</td>
      <td>22</td>
    </tr>
    <tr>
      <th>3</th>
      <td>David</td>
      <td>3</td>
      <td>40</td>
    </tr>
  </tbody>
</table>
</div>




```python
customer_df['Age']
```




    0    25
    1    30
    2    22
    3    40
    Name: Age, dtype: int64




```python
# Example: Dictionaries

person = {"name": "Nayeem",
          "age": 25,
          "is_student": True}
print("Person:", person)
print("Name:", person["name"])  # Access by key
person["age"] = 26  # Update value
print("Person:", person)
```

    Person: {'name': 'Nayeem', 'age': 25, 'is_student': True}
    Name: Nayeem
    Person: {'name': 'Nayeem', 'age': 26, 'is_student': True}
    

![image](https://github.com/user-attachments/assets/c09ae211-8a59-4df1-8275-9dc697d97991)


**Real-life Use Case:**

Storing structured data, such as user profiles or configurations.


```python
#Converting the Dictionary into a Dataframe
import pandas as pd

pd.DataFrame([person])
```





  <div id="df-713cb7f3-13a1-45f6-a2a8-9fa89a006f1c" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>name</th>
      <th>age</th>
      <th>is_student</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Alice</td>
      <td>26</td>
      <td>True</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-713cb7f3-13a1-45f6-a2a8-9fa89a006f1c')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-713cb7f3-13a1-45f6-a2a8-9fa89a006f1c button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-713cb7f3-13a1-45f6-a2a8-9fa89a006f1c');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


    </div>
  </div>




Dictionary values can be lists; so, to access individual attributes:

1. Retriev the **list** by looking up its **key**.
2. Retrieve the **list** element by using its **index**.


```python
# Looking up the stock quantity for skis

item_details = {'skis': [250, 12, 'in stock'],
                'snowboard': [220, 0, 'sold out'],
                'goggles': [100, 0, 'sold out'],
                'boots': [80, 5, 'in stock']}
item_details
```




    {'skis': [250, 12, 'in stock'],
     'snowboard': [220, 0, 'sold out'],
     'goggles': [100, 0, 'sold out'],
     'boots': [80, 5, 'in stock']}




```python
item_details['skis']
```




    [250, 12, 'in stock']




```python
item_details['skis'][1]
```




    12




```python
pd.DataFrame(item_details)
```





  <div id="df-bb11f43c-3a1a-4b4d-854a-52fb590501ec" class="colab-df-container">
    <div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>skis</th>
      <th>snowboard</th>
      <th>goggles</th>
      <th>boots</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>250</td>
      <td>220</td>
      <td>100</td>
      <td>80</td>
    </tr>
    <tr>
      <th>1</th>
      <td>12</td>
      <td>0</td>
      <td>0</td>
      <td>5</td>
    </tr>
    <tr>
      <th>2</th>
      <td>in stock</td>
      <td>sold out</td>
      <td>sold out</td>
      <td>in stock</td>
    </tr>
  </tbody>
</table>
</div>
    <div class="colab-df-buttons">

  <div class="colab-df-container">
    <button class="colab-df-convert" onclick="convertToInteractive('df-bb11f43c-3a1a-4b4d-854a-52fb590501ec')"
            title="Convert this dataframe to an interactive table."
            style="display:none;">

  <svg xmlns="http://www.w3.org/2000/svg" height="24px" viewBox="0 -960 960 960">
    <path d="M120-120v-720h720v720H120Zm60-500h600v-160H180v160Zm220 220h160v-160H400v160Zm0 220h160v-160H400v160ZM180-400h160v-160H180v160Zm440 0h160v-160H620v160ZM180-180h160v-160H180v160Zm440 0h160v-160H620v160Z"/>
  </svg>
    </button>

  <style>
    .colab-df-container {
      display:flex;
      gap: 12px;
    }

    .colab-df-convert {
      background-color: #E8F0FE;
      border: none;
      border-radius: 50%;
      cursor: pointer;
      display: none;
      fill: #1967D2;
      height: 32px;
      padding: 0 0 0 0;
      width: 32px;
    }

    .colab-df-convert:hover {
      background-color: #E2EBFA;
      box-shadow: 0px 1px 2px rgba(60, 64, 67, 0.3), 0px 1px 3px 1px rgba(60, 64, 67, 0.15);
      fill: #174EA6;
    }

    .colab-df-buttons div {
      margin-bottom: 4px;
    }

    [theme=dark] .colab-df-convert {
      background-color: #3B4455;
      fill: #D2E3FC;
    }

    [theme=dark] .colab-df-convert:hover {
      background-color: #434B5C;
      box-shadow: 0px 1px 3px 1px rgba(0, 0, 0, 0.15);
      filter: drop-shadow(0px 1px 2px rgba(0, 0, 0, 0.3));
      fill: #FFFFFF;
    }
  </style>

    <script>
      const buttonEl =
        document.querySelector('#df-bb11f43c-3a1a-4b4d-854a-52fb590501ec button.colab-df-convert');
      buttonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';

      async function convertToInteractive(key) {
        const element = document.querySelector('#df-bb11f43c-3a1a-4b4d-854a-52fb590501ec');
        const dataTable =
          await google.colab.kernel.invokeFunction('convertToInteractive',
                                                    [key], {});
        if (!dataTable) return;

        const docLinkHtml = 'Like what you see? Visit the ' +
          '<a target="_blank" href=https://colab.research.google.com/notebooks/data_table.ipynb>data table notebook</a>'
          + ' to learn more about interactive tables.';
        element.innerHTML = '';
        dataTable['output_type'] = 'display_data';
        await google.colab.output.renderOutput(dataTable, element);
        const docLink = document.createElement('div');
        docLink.innerHTML = docLinkHtml;
        element.appendChild(docLink);
      }
    </script>
  </div>


<div id="df-53d6eef0-1657-47a3-acfe-5238662b77d9">
  <button class="colab-df-quickchart" onclick="quickchart('df-53d6eef0-1657-47a3-acfe-5238662b77d9')"
            title="Suggest charts"
            style="display:none;">

<svg xmlns="http://www.w3.org/2000/svg" height="24px"viewBox="0 0 24 24"
     width="24px">
    <g>
        <path d="M19 3H5c-1.1 0-2 .9-2 2v14c0 1.1.9 2 2 2h14c1.1 0 2-.9 2-2V5c0-1.1-.9-2-2-2zM9 17H7v-7h2v7zm4 0h-2V7h2v10zm4 0h-2v-4h2v4z"/>
    </g>
</svg>
  </button>

<style>
  .colab-df-quickchart {
      --bg-color: #E8F0FE;
      --fill-color: #1967D2;
      --hover-bg-color: #E2EBFA;
      --hover-fill-color: #174EA6;
      --disabled-fill-color: #AAA;
      --disabled-bg-color: #DDD;
  }

  [theme=dark] .colab-df-quickchart {
      --bg-color: #3B4455;
      --fill-color: #D2E3FC;
      --hover-bg-color: #434B5C;
      --hover-fill-color: #FFFFFF;
      --disabled-bg-color: #3B4455;
      --disabled-fill-color: #666;
  }

  .colab-df-quickchart {
    background-color: var(--bg-color);
    border: none;
    border-radius: 50%;
    cursor: pointer;
    display: none;
    fill: var(--fill-color);
    height: 32px;
    padding: 0;
    width: 32px;
  }

  .colab-df-quickchart:hover {
    background-color: var(--hover-bg-color);
    box-shadow: 0 1px 2px rgba(60, 64, 67, 0.3), 0 1px 3px 1px rgba(60, 64, 67, 0.15);
    fill: var(--button-hover-fill-color);
  }

  .colab-df-quickchart-complete:disabled,
  .colab-df-quickchart-complete:disabled:hover {
    background-color: var(--disabled-bg-color);
    fill: var(--disabled-fill-color);
    box-shadow: none;
  }

  .colab-df-spinner {
    border: 2px solid var(--fill-color);
    border-color: transparent;
    border-bottom-color: var(--fill-color);
    animation:
      spin 1s steps(1) infinite;
  }

  @keyframes spin {
    0% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
      border-left-color: var(--fill-color);
    }
    20% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    30% {
      border-color: transparent;
      border-left-color: var(--fill-color);
      border-top-color: var(--fill-color);
      border-right-color: var(--fill-color);
    }
    40% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-top-color: var(--fill-color);
    }
    60% {
      border-color: transparent;
      border-right-color: var(--fill-color);
    }
    80% {
      border-color: transparent;
      border-right-color: var(--fill-color);
      border-bottom-color: var(--fill-color);
    }
    90% {
      border-color: transparent;
      border-bottom-color: var(--fill-color);
    }
  }
</style>

  <script>
    async function quickchart(key) {
      const quickchartButtonEl =
        document.querySelector('#' + key + ' button');
      quickchartButtonEl.disabled = true;  // To prevent multiple clicks.
      quickchartButtonEl.classList.add('colab-df-spinner');
      try {
        const charts = await google.colab.kernel.invokeFunction(
            'suggestCharts', [key], {});
      } catch (error) {
        console.error('Error during call to suggestCharts:', error);
      }
      quickchartButtonEl.classList.remove('colab-df-spinner');
      quickchartButtonEl.classList.add('colab-df-quickchart-complete');
    }
    (() => {
      let quickchartButtonEl =
        document.querySelector('#df-53d6eef0-1657-47a3-acfe-5238662b77d9 button');
      quickchartButtonEl.style.display =
        google.colab.kernel.accessAllowed ? 'block' : 'none';
    })();
  </script>
</div>

    </div>
  </div>





```python
# Membership Tests on Dictionary Keys

print('skis' in item_details)
print('stick' in item_details)
```

    True
    False
    


```python
# Modifying Dictionary

item_details['stick'] = [120, 8, 'in stock']
item_details
```




    {'skis': [250, 12, 'in stock'],
     'snowboard': [220, 0, 'sold out'],
     'goggles': [100, 0, 'sold out'],
     'boots': [80, 5, 'in stock'],
     'stick': [120, 8, 'in stock']}




```python
item_details['stick'] = [120, 0, 'sold out']
item_details
```




    {'skis': [250, 12, 'in stock'],
     'snowboard': [220, 0, 'sold out'],
     'goggles': [100, 0, 'sold out'],
     'boots': [80, 5, 'in stock'],
     'stick': [120, 0, 'sold out']}




```python
# Deleting Keys from Dictionary

del item_details['stick']
item_details
```




    {'skis': [250, 12, 'in stock'],
     'snowboard': [220, 0, 'sold out'],
     'goggles': [100, 0, 'sold out'],
     'boots': [80, 5, 'in stock']}


![image](https://github.com/user-attachments/assets/598c7f0e-0932-4dc0-adf5-dae3666c82a7)


```python
item_details.keys()
```




    dict_keys(['skis', 'snowboard', 'goggles', 'boots'])




```python
item_details.values()
```




    dict_values([[250, 12, 'in stock'], [220, 0, 'sold out'], [100, 0, 'sold out'], [80, 5, 'in stock']])




```python
# The .items() method returns key-value pairs from a dictionary as a list of tuples
item_details.items()
```




    dict_items([('skis', [250, 12, 'in stock']), ('snowboard', [220, 0, 'sold out']), ('goggles', [100, 0, 'sold out']), ('boots', [80, 5, 'in stock'])])



The .get() method returns the values associated with a dictionary key:
- It won't return a KeyError if the key isn't found.
- You can specify an optional value to return if the key is not found.


```python
item_details.get('skis')
```




    [250, 12, 'in stock']




```python
item_details.get('football')
```
![image](https://github.com/user-attachments/assets/53dcb37c-5474-488e-ac99-157395d58063)


**7. Sets (set):**

* Unordered collection of **unique items**, which means their values cannot be accessed via index or key.
* Sets are mutable (values can be added/removed), but set values must be unique & immutable
* Useful for operations like union, intersection, and difference.


```python
# Example: Sets

unique_numbers = {1, 2, 3, 3, 4}  # Duplicates are removed
print("Unique Numbers:", unique_numbers)
```

    Unique Numbers: {1, 2, 3, 4}
    

**Real-life Use Case:**

Removing duplicates from a list or checking membership.

![image](https://github.com/user-attachments/assets/286d95df-9972-4c62-8510-21527665f6be)






```python
friday_items = {'snowboard', 'snowboard', 'skis', 'snowboard', 'stick'}
saturday_items = {'goggles', 'helmet', 'snowboard', 'skis', 'goggles'}

print("Union Output: ", friday_items.union(saturday_items))
print("Intersection Output: ", friday_items.intersection(saturday_items))
print("Difference Output: ", friday_items.difference(saturday_items))
print("Symmetric Difference Output: ", friday_items.symmetric_difference(saturday_items))
```

    Union Output:  {'snowboard', 'skis', 'helmet', 'goggles', 'stick'}
    Intersection Output:  {'snowboard', 'skis'}
    Difference Output:  {'stick'}
    Symmetric Difference Output:  {'helmet', 'goggles', 'stick'}
    

**8. None (NoneType):**

* Represents the absence of a value.

* Often used as a placeholder.


```python
# Example: None

result = None
print("Result:", result)
```

    Result: None
    

**Real-life Use Case:**

Initializing a variable before assigning a value.

##**4. Iterables and Mutability:**

**Iterables** are data types that can be iterated, or looped through, allowing you to move from one value to the next.

**These data types are considered iterable:**

**Sequence, Mapping, Set, Text** (While text strings are treated as a single value, individual characters in a text string can be iterated through).

**Mutability:** Whether an object can be changed after creation.

*   **Mutable:** Lists, dictionaries, sets.
*   **Immutable:** Strings, tuples, integers, floats.


```python
# Example: Mutability

# List (Mutable)
colors = ["red", "green", "blue"]
colors[0] = "yellow"
print("Updated Colors:", colors)
```

    Updated Colors: ['yellow', 'green', 'blue']
    


```python
# Tuple (Immutable)
rgb = ("red", "green", "blue")
rgb[0] = "yellow"  # This will raise an error
```


    ---------------------------------------------------------------------------

    TypeError                                 Traceback (most recent call last)

    <ipython-input-24-8ecafad6bed9> in <cell line: 0>()
          1 # Tuple (Immutable)
          2 rgb = ("red", "green", "blue")
    ----> 3 rgb[0] = "yellow"  # This will raise an error
    

    TypeError: 'tuple' object does not support item assignment


**Real-life Use Case:**

Use lists for dynamic data and tuples for fixed data.

## **5. List vs. Tuples:**
![image](https://github.com/user-attachments/assets/c58bd1b4-ddba-4bb9-8e42-b2dd24e64953)


## 6. Exercise:

* Create a list of their favorite foods and print the second item.

* Create a dictionary to store their name, age, and favorite color.

* Convert a list of numbers into a set to remove duplicates.
