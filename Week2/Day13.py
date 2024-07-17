#  Regular Expressions and File I/O
"""
Objectives
 - Understand and use regular expressions for pattern matching.
 - Learn about file I/O operations in Python.
"""
# --------Regular Expressions--------
"""
 - Understand and use regular expressions for pattern matching.
 - Learn about file I/O operations in Python.

 What are Regular Expressions?
    Regular expressions (regex) are sequences of characters that form search patterns. They can be used for string matching and manipulation.
"""
# Example
import re

pattern = r"\d+"  # Matches one or more digits
text = "There are 123 apples and 45 oranges."
matches = re.findall(pattern, text)
print(matches)  # Output: ['123', '45']


# --------File I/O--------
# Reading from a File:
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)

# Writing to a File:
# with open("output.txt", "w") as file:
#     file.write("Hello World!")


# CHALLENGE
# Write a program that reads a large text file and counts the frequency of each word using regular expressions.
from collections import Counter

def count_words(filename):
    with open(filename, "r") as file:
        text = file.read()
        words = re.findall(r"\b\w+\b", text.lower())
        return Counter(words)

word_counts = count_words("text_file.txt")
with open("word_counts.txt", "w") as output_file:
    for word, count in word_counts.items():
        output_file.write(f"{word}: {count}\n")
