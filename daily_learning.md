# Python Daily Learning 🚀

My daily Python learning journey.

## Progress

This repository contains my daily Python learning concepts, examples, and practice.

---

## Day 1 — Variables

**Date:** 2026-09-17


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


---

## Day 2 — Data Types

**Date:** 2026-09-18


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


---

## Day 3 — Strings

**Date:** 2026-09-19


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


---

## Day 4 — Lists

**Date:** 2026-09-20


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


---

## Day 5 — Tuples

**Date:** 2026-09-21


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


---

## Day 6 — Sets

**Date:** 2026-09-22


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


---

## Day 7 — Dictionaries

**Date:** 2026-09-23


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


---

## Day 8 — Input

**Date:** 2026-09-24


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


---

## Day 9 — Operators

**Date:** 2026-09-25


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


---

## Day 10 — If Else

**Date:** 2026-09-26


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


---

## Day 11 — For Loop

**Date:** 2026-09-27


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


---

## Day 12 — While Loop

**Date:** 2026-09-28


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


---

## Day 13 — Functions

**Date:** 2026-09-29


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


---

## Day 14 — Lambda Functions

**Date:** 2026-09-30


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


---

## Day 15 — List Comprehension

**Date:** 2026-10-01


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


---

## Day 16 — Exception Handling

**Date:** 2026-10-02


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


---

## Day 17 — File Handling

**Date:** 2026-10-03


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


---

## Day 18 — Modules

**Date:** 2026-10-04


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


---

## Day 19 — Classes and Objects

**Date:** 2026-10-05


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


---

## Day 20 — Inheritance

**Date:** 2026-10-06


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


---

## Day 21 — Generators

**Date:** 2026-10-07


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


---

## Day 22 — Regular Expressions

**Date:** 2026-10-08


### What are Regular Expressions?

Regular expressions are used to search for patterns in text.

### Example

import re

text = "My phone number is 9876543210"

result = re.search(r"\d{10}", text)

print(result.group())

### Output

9876543210

### Real Life Example

Regex can be used to validate emails, phone numbers and other text patterns.

### Practice

Find an email address inside a string using regex.


---

## Day 23 — NumPy

**Date:** 2026-10-09


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


---
