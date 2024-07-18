# Testing and Debugging
"""
*Objectives
 - Understand the importance of testing and debugging in software development.
 - Learn how to write unit tests in Python.
 - Get familiar with debugging techniques and tools.
 - Learning Content

* 1. Testing
?Why Testing is Important:
 - Ensures code correctness.
 - Helps identify bugs and issues early.
 - Improves code quality and reliability.

?Types of Testing:
 1.Unit Testing: Testing individual units or components of the code.
 2.Integration Testing: Testing how different components work together.
 3.Functional Testing: Testing the functionality of the software.
4. Regression Testing: Ensuring new changes don't break existing functionality.

"""
#?Unit Testing in Python:
"""
 - Using the unittest module.
 - Writing test cases.
 - Running tests and interpreting results.
"""
# Example 
import unittest

def addUt(a, b): #! changed from add() to addTe() to avoid depreciated methods on challenge
    return a + b

class TestMathFunc(unittest.TestCase):
    def test_addUt(self):
        self.assertEqual(addUt(3,2), 5)
        self.assertEqual(addUt(-1, 1), 0)
        self.assertEqual(addUt(-1, -1), -2)


if __name__ == "__name__":
    unittest.main()




#* 2. Debugging
"""
?Why Debugging is Important:
 - Identifies and fixes bugs.
 - Helps understand code behavior.
 - Improves code performance and reliability.

?Debugging Techniques:
 1.Print Statements: Simple but effective for small-scale debugging.
 2.Using a Debugger: Tools like pdb (Python Debugger) for more advanced debugging.
 3.Analyzing Error Messages: Understanding stack traces and error messages to pinpoint issues.
"""
# Example using pdb
import pdb

def faulty_function(a, b):
    result = a + b
    # pdb.set_trace() #* sets a breakpoint
    result = result / (a - b)
    return result

print(faulty_function(2, 1))



#* CHALLENGE
"""
Write a program that simulates a simple calculator. Include functions for addition, subtraction, multiplication, and division. Write unit tests for each function and debug any issues you encounter.
"""
#Todo: Calculator Program

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    else:
        return a / b
    


print("Choose operation")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

choice = input("Enter choice (1,2,3,4): ")


num1 = float(input("Enter first number: "))
num2 = float(input("Enter Second number: "))

if choice == "1":
    print(f"{num1} + {num2} = {add(num1, num2)}")
elif choice == "2":
    print(f"{num1} - {num2} = {subtract(num1, num2)}")
elif choice == "3":
    print(f"{num1} x {num2} = {multiply(num1, num2)}")
elif choice == "2":
    print(f"{num1} / {num2} = {divide(num1, num2)}")
else:
    print("Invalid input")


#Todo: Unit Tests
class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(-1, -1), -2)

    def test_subtract(self):
        self.assertEqual(subtract(2, 3), -1)
        self.assertEqual(subtract(-1, 1), -2)
        self.assertEqual(subtract(-1, -1), 0)

    def test_multiply(self):
        self.assertEqual(multiply(2, 3), 6)
        self.assertEqual(multiply(-1, 1), -1)
        self.assertEqual(multiply(-1, -1), 1)

    def test_divide(self):
        self.assertEqual(divide(6, 3), 2)
        self.assertEqual(divide(-1, 1), -1)
        self.assertEqual(divide(-1, -1), 1)
        with self.assertRaises(ValueError):
            divide(1, 0)


unittest.main()