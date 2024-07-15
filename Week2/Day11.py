# Error Handling and Testing
"""
Objectives
- Understand how to handle errors and exceptions in Python.
- Learn how to write and run tests to ensure code correctness.
"""
# --------Error Handling--------
"""
Exception Handling
Exception handling allows a program to deal with unexpected situations (errors) without crashing.

Common Exceptions:
ZeroDivisionError, TypeError, ValueError, IndexError, etc.
"""
# Example
try:
    # Code that might raise an exception
    num = int(input("Enter a number: "))
    result = 10 / num
    print(f"The result is {result}")
except ZeroDivisionError:
    #  Code that runs if the ZeroDIvisionError occurs
    print("You can't divide by zero!")
except ValueError:
    #  Code that runs if the ValueError occurs
    print("Please enter a valid number!")
finally:
    # Code that runs no matter what (optional)
    print("This will run no matter what")



"""
Raise an exception
As a Python developer you can choose to throw an exception if a condition occurs.

To throw (or raise) an exception, use the `raise` keyword.
"""
# Example
# Raise an error and stop the program if x is lower than 0:
x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

"""
The raise keyword is used to raise an exception.

You can define what kind of error to raise, and the text to print to the user.
"""
# Example
# Raise a TypeError if x is not an integer:
x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")



# --------Testing--------
"""
Writing Test Cases
Why Testing?

To ensure that your code works correctly and handles edge cases.
"""
# Using unittest Module
import unittest

def add(a, b):
    return a + b

class TestMathFunctions(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

if __name__ == '__main__':
    unittest.main()




"""
CHALLENGE
Write a program that performs a division operation. The program should:

1.Prompt the user to enter two numbers.
2.Handle ZeroDivisionError if the second number is zero.
3.Handle ValueError if the user enters something that is not a number.
4.Include test cases for the division function using the unittest module.
"""

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "You can't divide by zero!"
    except ValueError:
        return "Invalid input! Please enter numbers only."


class TestDivision(unittest.TestCase):
    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(10, 0), "You can't divide by zero!")
        self.assertEqual(divide('a', 1), "Invalid input! Please enter numbers only.")

if __name__ == '__main__':
    unittest.main()
