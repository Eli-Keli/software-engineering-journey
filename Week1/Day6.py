# Data Structures - Sets and Tuples

# SETS

# Creating a Set
my_set = {1, 2, 3, 4, 5}

# Basic Operations:
# - Add elements: my_set.add(5)
# - Remove elements: my_set.remove(3)
# - Set operations: union (set1 | set2), intersection (set1 & set2), difference (set1 - set2)

# Example
fruits = {"apple", "mango", "banana"}
fruits.add("orange")
fruits.remove("banana")
more_fruits = {"grape", "melon"}
all_fruits = fruits | more_fruits
print(all_fruits)  


# TUPLES

# Creating a Tuple
my_tuple = (1, 2, 3, 4)

# Basic Operations:
# - Access elements: my_tuple[0]
# - Tuples are immutable, so you cannot add or remove elements.

# Example
person = ("Alice", 25, "New York")
print(person[0])  
print(person[1:])




#CHALLENGE:

# Set Operations:
# - Write a program that performs various set operations (union, intersection, difference) on two given sets and displays the results.

# Tuple Manipulation:
# - Write a program that takes a tuple of numbers and returns a new tuple with only the even numbers.

set1 = {22, 35, 17, 31}
set2 = {13, 26, 18, 9}

unionSet = set1 | set2
print(unionSet)

intersectionSet = set1 & set2
print(intersectionSet)

setDifference = set1 - set2
print(setDifference)



num_tuple = (4, 15, 7, 13, 6, 12, 24, 21)

# Use a list comprehension to filter even numbers and then convert it back to a tuple
even_number_tuple = tuple(num for num in num_tuple if num%2 == 0)
print(even_number_tuple)


