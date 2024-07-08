# LISTS

# Create a list
fruits = ["apple", "mango", "banana", "cherry"]

# Access elements
print(fruits[0])

# Modify elements
fruits[1] = "blueberry"
print(fruits)

# Add elements
fruits.append("pineapple")
print(fruits)

# Remove elements
fruits.remove("blueberry")
print(fruits)

# Iterate over elements
for fruit in fruits:
    print(fruit)

# Get number of elements
lenght_fruits = len(fruits)
print(lenght_fruits)

# ---------------List Methods-------------------

# Create a new list
new_fruits = ["apple", "banana", "cherry"]
print("Original list:", new_fruits)

# Append: Adds an element to the end of the list.
new_fruits.append("date")
print("After append:", new_fruits)

# Extend: Adds all elements of an iterable (like another list) to the end of the list.
new_fruits.extend(["elderberry", "fig"])
print("After extend:", new_fruits)

# Insert: Inserts an element at a specified position.
new_fruits.insert(1, "blueberry")
print("After insert:", new_fruits)

# Remove: Removes the first occurrence of a specified element.
new_fruits.remove("banana")
print("After remove:", new_fruits)

# Pop:  Removes and returns the element at a specified position (or the last element if no position is specified).
popped_fruit = new_fruits.pop()
print("Popped fruit:", popped_fruit)
print("After pop:", new_fruits)

# Index: Returns the index of the first occurrence of a specified element.
index = new_fruits.index("cherry")
print("Index of 'cherry':", index)

# Count: Returns the number of occurrences of a specified element.
count = new_fruits.count("apple")
print("Count of 'apple':", count)

# Sort:  Sorts the list in ascending order (or descending order if specified).
new_fruits.sort()
print("After sort:", new_fruits)

# Reverse: Reverses the elements of the list.
new_fruits.reverse()
print("After reverse:", new_fruits)

# Copy: Returns a shallow copy of the list.
new_fruits_copy = new_fruits.copy()
print("Copy of new_fruits:", new_fruits_copy)

# Concatenation: Use the + operator to concatenate two lists.
more_new_fruits = ["grape", "honeydew"]
all_new_fruits = new_fruits + more_new_fruits
print("After concatenation:", all_new_fruits)

# Repetition: Use the * operator to repeat a list a specified number of times.
repeated_new_fruits = new_fruits * 2
print("After repetition:", repeated_new_fruits)

# Membership: Use the in operator to check if an element is in the list.
is_banana_there = "banana" in new_fruits
print("Is 'banana' in new_fruits?", is_banana_there)

# Length: Use the len() function to get the number of elements in the list.
length = len(new_fruits)
print("Length of new_fruits:", length)

# Indexing: Use square brackets [] to access elements by index.
first_fruit = new_fruits[0]
print("First fruit:", first_fruit)

# Slicing: Use the slice notation : to access a range of elements.
sliced_new_fruits = new_fruits[1:3]
print("Sliced new_fruits:", sliced_new_fruits)




# CHALLENGE: Write a program that reverses a list/array. For example, given [1, 2, 3, 4, 5], the program should return [5, 4, 3, 2, 1].

ages = [34, 23, 19, 41, 27]
ages.reverse()
print("Ages reversed: ", ages)

