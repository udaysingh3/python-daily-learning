from datetime import datetime

topics = [
    {
        "title": "Variables",
        "content": """
### What is a Variable?

A variable is used to store a value in Python.

### Syntax

name = value

### Example

name = "Uday"
age = 21

print(name)
print(age)

### Output

Uday
21

### Real Life Example

A student's name and age can be stored in variables.

### Important Point

Python automatically detects the data type.

### Practice

Create variables for your name, age and college.
"""
    },

    {
        "title": "Data Types",
        "content": """
### What are Data Types?

Data types tell Python what type of value is stored.

### Main Data Types

int
float
str
bool
list
tuple
set
dict

### Example

name = "Uday"
age = 21
height = 5.8
student = True

print(type(name))
print(type(age))
print(type(height))
print(type(student))

### Output

<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>

### Real Life Example

Age is generally an integer, height can be a float, and student status can be True or False.

### Practice

Create variables using int, float, string and boolean.
"""
    },

    {
        "title": "Strings",
        "content": """
### What is a String?

A string is text written inside quotes.

### Example

name = "Uday"

print(name)
print(name[0])
print(name.upper())

### Output

Uday
U
UDAY

### Real Life Example

Names, addresses and messages are commonly stored as strings.

### Important Point

String indexing starts from 0.

### Practice

Create your full name and print the first character.
"""
    },

    {
        "title": "Lists",
        "content": """
### What is a List?

A list stores multiple values in one variable.

### Example

fruits = ["Apple", "Banana", "Mango"]

print(fruits)
print(fruits[0])

### Output

['Apple', 'Banana', 'Mango']
Apple

### Real Life Example

A shopping list can be stored using a Python list.

### Important Point

Lists are ordered and mutable.

### Practice

Create a list of five programming languages.
"""
    },

    {
        "title": "Tuples",
        "content": """
### What is a Tuple?

A tuple is a collection of values that cannot normally be changed.

### Example

numbers = (10, 20, 30)

print(numbers)
print(numbers[0])

### Output

(10, 20, 30)
10

### Real Life Example

Coordinates such as (10, 20) can be stored as a tuple.

### Important Point

Tuples are immutable.

### Practice

Create a tuple containing five numbers.
"""
    },

    {
        "title": "Sets",
        "content": """
### What is a Set?

A set stores unique values.

### Example

numbers = {1, 2, 2, 3, 4}

print(numbers)

### Output

{1, 2, 3, 4}

### Real Life Example

A set can be useful when you want to remove duplicate values.

### Important Point

Sets do not store duplicate values.

### Practice

Create a set containing duplicate numbers.
"""
    },

    {
        "title": "Dictionaries",
        "content": """
### What is a Dictionary?

A dictionary stores data using key-value pairs.

### Example

student = {
    "name": "Uday",
    "age": 21,
    "course": "B.Tech CSE"
}

print(student["name"])
print(student["course"])

### Output

Uday
B.Tech CSE

### Real Life Example

Student information can be represented using a dictionary.

### Practice

Create a dictionary containing your name, age and college.
"""
    },

    {
        "title": "Input",
        "content": """
### What is input()?

input() is used to take information from the user.

### Example

name = input("Enter your name: ")

print("Hello", name)

### Example Output

Enter your name: Uday
Hello Uday

### Real Life Example

A login form takes information from the user.

### Important Point

input() normally returns a string.

### Practice

Take the user's name and age as input.
"""
    },

    {
        "title": "Operators",
        "content": """
### What are Operators?

Operators are symbols used to perform operations.

### Example

a = 10
b = 3

print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a % b)

### Output

13
7
30
3.3333333333333335
1

### Real Life Example

A calculator uses arithmetic operations.

### Practice

Create two numbers and perform all arithmetic operations.
"""
    },

    {
        "title": "If Else",
        "content": """
### What is If Else?

If-else is used to make decisions.

### Example

age = 20

if age >= 18:
    print("Adult")
else:
    print("Minor")

### Output

Adult

### Real Life Example

A website can check whether a user is old enough to access a service.

### Important Point

Python uses indentation.

### Practice

Check whether a number is positive or negative.
"""
    },

    {
        "title": "For Loop",
        "content": """
### What is a For Loop?

A for loop repeats code for each item in a sequence.

### Example

for i in range(1, 6):
    print(i)

### Output

1
2
3
4
5

### Real Life Example

A program can use a loop to process every student in a class.

### Practice

Print numbers from 1 to 10 using a for loop.
"""
    },

    {
        "title": "While Loop",
        "content": """
### What is a While Loop?

A while loop runs while a condition is true.

### Example

number = 1

while number <= 5:
    print(number)
    number += 1

### Output

1
2
3
4
5

### Real Life Example

A game can continue running while the player is alive.

### Practice

Print numbers from 10 to 1 using a while loop.
"""
    },

    {
        "title": "Functions",
        "content": """
### What is a Function?

A function is a reusable block of code.

### Syntax

def function_name():
    code

### Example

def greet():
    print("Hello Uday!")

greet()

### Output

Hello Uday!

### Real Life Example

A payment system can have a function called make_payment().

### Practice

Create a function that adds two numbers.
"""
    },

    {
        "title": "Lambda Functions",
        "content": """
### What is a Lambda Function?

A lambda function is a small anonymous function.

### Syntax

lambda arguments: expression

### Example

square = lambda x: x * x

print(square(5))

### Output

25

### Practice

Create a lambda function that adds two numbers.
"""
    },

    {
        "title": "List Comprehension",
        "content": """
### What is List Comprehension?

List comprehension provides a short way to create lists.

### Example

numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)

### Output

[1, 4, 9, 16, 25]

### Practice

Create a list containing squares from 1 to 10.
"""
    },

    {
        "title": "Exception Handling",
        "content": """
### What is Exception Handling?

Exception handling allows us to handle errors safely.

### Example

try:
    number = int(input("Enter a number: "))
    print(10 / number)

except ZeroDivisionError:
    print("Cannot divide by zero")

except ValueError:
    print("Please enter a valid number")

### Real Life Example

Banking applications need error handling so one wrong input does not crash the complete application.

### Practice

Write a program that handles invalid input.
"""
    },

    {
        "title": "File Handling",
        "content": """
### What is File Handling?

File handling allows Python to read and write files.

### Example

with open("example.txt", "w") as file:
    file.write("Hello Python")

with open("example.txt", "r") as file:
    print(file.read())

### Output

Hello Python

### Real Life Example

Applications can save user information in files.

### Practice

Create a file and write your name into it.
"""
    },

    {
        "title": "Modules",
        "content": """
### What is a Module?

A module is a Python file containing reusable code.

### Example

import math

print(math.sqrt(25))
print(math.pi)

### Output

5.0
3.141592653589793

### Real Life Example

Instead of writing mathematical functions yourself, you can use Python's math module.

### Practice

Use the math module to find the square root of 100.
"""
    },

    {
        "title": "Classes and Objects",
        "content": """
### What is a Class?

A class is a blueprint for creating objects.

### Example

class Student:
    def __init__(self, name):
        self.name = name

student = Student("Uday")

print(student.name)

### Output

Uday

### Real Life Example

A Student class can represent students in a college management system.

### Practice

Create a Student class with name and age.
"""
    },

    {
        "title": "Inheritance",
        "content": """
### What is Inheritance?

Inheritance allows one class to use features of another class.

### Example

class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

dog = Dog()
dog.speak()

### Output

Animal speaks

### Real Life Example

A Car class can inherit common features from a Vehicle class.

### Practice

Create a Vehicle class and a Car child class.
"""
    },

    {
        "title": "Generators",
        "content": """
### What is a Generator?

A generator produces values one at a time using yield.

### Example

def numbers():
    for i in range(1, 4):
        yield i

for number in numbers():
    print(number)

### Output

1
2
3

### Important Point

Generators can save memory.

### Practice

Create a generator that produces numbers from 1 to 10.
"""
    },

    {
        "title": "Regular Expressions",
        "content": """
### What are Regular Expressions?

Regular expressions are used to search for patterns in text.

### Example

import re

text = "My phone number is 9876543210"

result = re.search(r"\\d{10}", text)

print(result.group())

### Output

9876543210

### Real Life Example

Regex can be used to validate emails, phone numbers and other text patterns.

### Practice

Find an email address inside a string using regex.
"""
    },

    {
        "title": "NumPy",
        "content": """
### What is NumPy?

NumPy is a Python library used for numerical computing.

### Example

import numpy as np

numbers = np.array([1, 2, 3, 4, 5])

print(numbers)
print(numbers * 2)

### Output

[1 2 3 4 5]
[ 2  4  6  8 10]

### Real Life Example

NumPy is widely used in data science and machine learning.

### Practice

Create a NumPy array containing numbers from 1 to 10.
"""
    },

    {
        "title": "Pandas",
        "content": """
### What is Pandas?

Pandas is a Python library used for data analysis.

### Example

import pandas as pd

data = {
    "Name": ["Uday", "Rahul"],
    "Age": [21, 22]
}

df = pd.DataFrame(data)

print(df)

### Real Life Example

Pandas can be used to analyze CSV files and datasets.

### Practice

Create a DataFrame containing five students and their marks.
"""
    },

    {
        "title": "JSON",
        "content": """
### What is JSON?

JSON is commonly used to store and exchange data.

### Example

import json

data = {
    "name": "Uday",
    "age": 21
}

json_data = json.dumps(data)

print(json_data)

### Output

{"name": "Uday", "age": 21}

### Real Life Example

Web APIs commonly send and receive JSON data.

### Practice

Create a dictionary and convert it into JSON.
"""
    },

    {
        "title": "APIs with Python",
        "content": """
### What is an API?

An API allows different software applications to communicate.

### Example

import requests

response = requests.get("https://api.github.com")

print(response.status_code)

### Real Life Example

A weather application can use an API to get current weather data.

### Important Point

HTTP status code 200 generally means success.

### Practice

Learn how GET and POST requests work.
"""
    },

    {
        "title": "Virtual Environment",
        "content": """
### What is a Virtual Environment?

A virtual environment creates an isolated Python environment for a project.

### Create Environment

python -m venv .venv

### Activate on Windows

.venv\\Scripts\\activate

### Real Life Example

Different projects may require different versions of packages.

### Practice

Create a virtual environment for a Python project.
"""
    },

    {
        "title": "Python Packages",
        "content": """
### What is a Python Package?

A package contains reusable Python code.

### Example

pip install pandas

Then:

import pandas as pd

### Real Life Example

Developers use packages such as NumPy, Pandas and Requests instead of writing everything from scratch.

### Practice

Install NumPy and create a simple array.
"""
    }
]


def get_next_topic():
    try:
        with open("daily_learning.md", "r", encoding="utf-8") as file:
            content = file.read()

        completed_topics = content.count("## Day")

    except FileNotFoundError:
        completed_topics = 0

    return completed_topics % len(topics)


def generate_learning():
    index = get_next_topic()
    topic = topics[index]

    try:
        with open("daily_learning.md", "r", encoding="utf-8") as file:
            content = file.read()

    except FileNotFoundError:
        content = "# Python Daily Learning\n\n"

    day = content.count("## Day") + 1
    date = datetime.now().strftime("%Y-%m-%d")

    new_learning = f"""
## Day {day} — {topic['title']}

**Date:** {date}

{topic['content']}

---
"""

    with open("daily_learning.md", "a", encoding="utf-8") as file:
        file.write(new_learning)


if __name__ == "__main__":
    generate_learning()
