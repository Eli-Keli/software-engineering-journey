# Recursion and Advanced Functions

# Objectives
# - Understand recursion and how to use it.
# - Learn about advanced functions, including lambda functions, map, filter, and reduce.


# ----------Recursion----------
# A recursion is a function that calls itself to solve smaller instances of the same problem. 
# Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result.
# The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming.


# Example 1
def factorial(n):

    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5)) # Outputs 120


# Example 2
def tri_recursion(k):
    if k > 0:
        return k + tri_recursion(k-1)
    else:
        return 0
    
print(tri_recursion(5)) # output 15
# In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0).


# Base Case and Recursive Case
#   Base Case: The condition under which the recursion ends.
#   Recursive Case: The part of the function where the function calls itself.




# ----------Lambda Functions----------
# Anonymous Functions: Functions defined without a name using the lambda keyword.

# Syntax
lambda arguments: "expression"

# Example
add = lambda a, b: a + b
print(add(5, 3)) # output 8




# ----------Map, Filter and Reduce----------

numbers = [2, 3, 4, 5, 6, 7, 8, 9]
# Map: Applies a function to all items in an input list
# Example
squared = list(map(lambda x: x**2, numbers))
print(squared) # output [4, 9, 16, 25, 36, 49, 64, 81]

# Filter: Filters items out of a list based on a function that returns True or False
# Example
even = list(filter(lambda x: x%2==0, numbers))
print(even) # output [2, 4, 6, 8]

# Reduce: Applies a rolling computation to sequential pairs of values in a list.
# Example
from functools import reduce
product = reduce(lambda x, y: x*y, numbers)
print(product) # output 362880



# CHALLENGE: Write a program that uses recursion to solve a problem, such as the Tower of Hanoi or generating all permutations of a string.

# ----Tower of Hanoi Problem----
# The Tower of Hanoi is a puzzle consisting of three rods and a number of disks of different sizes, which can slide onto any rod. The puzzle starts with the disks neatly stacked in ascending order of size on one rod, the smallest at the top, making a conical shape. The objective of the puzzle is to move the entire stack to another rod, obeying the following simple rules:
# 1.Only one disk can be moved at a time.
# 2.Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack or on an empty rod.
# 3.No disk may be placed on top of a smaller disk.

#      Recursive Solution
# The recursive solution to the Tower of Hanoi problem can be summarized in the following steps:
# 1.Move the top n-1 disks from the source rod to the auxiliary rod.
# 2.Move the nth disk from the source rod to the target rod.
# 3.Move the n-1 disks from the auxiliary rod to the target rod.
# 4.The base case for the recursion is when there is only one disk to move. In that case, you simply move the disk from the source rod to the target rod.

def hanoi(n, source, auxiliary, target):
    if n > 0:
        # Move n-1 disks from source to auxiliary
        hanoi(n-1, source, target, auxiliary)

        # Move the nth disk from source to target
        print(f"Move disk {n} from {source} to {target}")

        # Move n-1 disks from auxiliary to target
        hanoi(n - 1, auxiliary, source, target)

# Example usage: Move 3 disks from rod A to rod C using B as auxiliary
hanoi(3, 'A', 'B', 'C')

