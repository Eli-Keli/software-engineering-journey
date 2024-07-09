# DICTIONARIES
# Key Concepts
# 1. Unordered Collection: Dictionaries store data in key-value pairs but do not maintain order.
# 2. Mutable: You can change dictionaries by adding, modifying, or removing elements.
# 3. Keys and Values: Keys must be unique and immutable (e.g., strings, numbers, tuples), while values can be of any data type.

# Create a dictonary
person = {
    "name": "Clifford",
    "age": 26,
    "city": "New York"
}

# Access elements
print(person["name"])

# Modify elements
person["age"] = 23
print(person)

# Add elements
person["email"] = "clifford@gmail.com"
print(person)

# Remove elements
del person["city"]
print(person)

# Iterate over elements
for key, value in person.items():
    print(f"{key}: {value}")


# CHALLENGE: Write a program that counts the occurrences of each word in a given text and stores the counts in a dictionary. The program should ignore spaces and consider both uppercase and lowercase letters as the same (i.e., 'A' and 'a' should be counted together).

frequency = {}

text = "Hello Word!".lower()
print(text)

for char in text:
    if char.isalpha(): # check if char is a letter
        if char in frequency:
            frequency[char] += 1
        else: 
            frequency[char] = 1


for key, value in frequency.items():
    print(f"{key}: {value}")


# -----------------Dictionary Comprehensions-----------------------------

# Create a dictionary where keys are numbers and values are their squares
squares = {x: x*x for x in range(1, 6)}
print(squares)


# Example: Combining Dictionary Methods and Comprehensions

# Create a new dictionary
newPerson = {
    "name": "Alice",
    "age": 25,
    "city": "New York",
    "email": "alice@gmail.com"
}

# Use items() to iterate over key-value pairs
for key, value in newPerson.items():
    print(f"{key}: {value}")

# Use keys() to iterate over keys
for key in newPerson.keys():
    print(key)

# Use values() to iterate over values
for value in newPerson.values():
    print(value)

# Use get() to retrieve a value with a default if key is not found
country = newPerson.get("country", "Unknown")
print(f"Country: {country}")

# Use setdefault() to add a key if it does not exist
newPerson.setdefault("country", "USA")
print(person)

# Use update() to merge another dictionary
updates = {"phone": "123-456-7890", "email": "alicenew@example.com"}
newPerson.update(updates)
print(newPerson)

# Dictionary comprehension to filter out keys with a specific prefix
filteredPerson = {
    key: value 
    for key, value in newPerson.items()
        if not key.startswith("e")
}
print(filteredPerson)