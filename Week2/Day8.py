# Functions and Modules

# Objectives:
# - Understand how to define and use functions.
# - Learn about modules and how to import them.

# Tasks:
# 1.Define and Call Functions:
#  - Learn how to create a function using the def keyword.
#  - Understand how to pass parameters and return values.

# 2.Explore Built-in Functions and Standard Library:
#  - Use built-in functions like len(), sum(), max(), etc.
#  - Import and use standard library modules like math, random, etc.

# 3. Create and Import Custom Modules:
#  - Create a custom module with some utility functions.
#  - Import and use the custom module in a program.


# ---------- Defining and Calling Functions----------

def greet(name):
    return f"Hello {name}!"

def sumf(a, b):
    return a + b

print(greet("Clifford"))
print(sumf(6, 3))


# ---------- Built-in Functions and Standard Library ----------
numbers = [5, 7, 9, 6, 8, 4]

print(f"Length of numbers: {len(numbers)}")
print(f"Sum of numbers: {sum(numbers)}")
print(f"Max number: {max(numbers)}")

import math

print(f"Square root of 16: {math.sqrt(16)}")
print(f"Factorial of 5: {math.factorial(5)}")

# ---------- Creating and Importing a Custom Module ----------
# CHALLENGE:
# Write a program that includes a custom module for mathematical operations (e.g., add, subtract, multiply, divide).
import math_operations as math0

print(f"Addition: {math0.add(10, 5)}")
print(f"Subtraction: {math0.subtract(10, 5)}")
print(f"Multiplication: {math0.multiply(10, 5)}")
print(f"Division: {math0.divide(10, 5)}")