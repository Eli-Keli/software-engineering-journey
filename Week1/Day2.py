# BASIC SYNTAX

# Variables and Data types
name = "Eli"
age = 17
height = 5.9
is_student = True

# Operators
sum_age = age + 1
height_squared = height * height

print(f"Name: {name}, Age: {age}, Height: {height}, Is Student: {is_student}")
print(f"Sum of Age: {sum_age}, Height Squared: {height_squared},")



# Write a program that takes user input and performs basic arithmetic operations (addition, subtraction, multiplication, and division).

# Arithmetic Operations Program 
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

# addition
addition = num1 + num2
# subtraction
subtraction =  num1 - num2
# multiplication
multiplication = num1 * num2
# division
division = num1 / num2 if num2 != 0 else "Error(division by zero)"

print(f"Addition: {addition}")
print(f"Subtraction: {subtraction}")
print(f"Multiplication: {multiplication}")
print(f"Division: {division}")


