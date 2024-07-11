# Files and Exception Handling

# --------File Handling------------

# opening a file
file = open("example.txt", "r") # 'r' for read mode

# reading a file
content = file.read()
print(content)

# writing to a file
with open("output.txt", "w") as file: # 'w' for write mode
    file.write("Hello World!")


# --------Exception Handling------------

# try-except block
try:
    result = 10/0
except ZeroDivisionError:
    print("Cannot divide number by zero")

# finally block
try:
    file = open("finally.txt", "r")
except FileNotFoundError:
    print("File not found!")
finally:
    file.close()


# --------CHALLENGE------------
# Write a program that reads a text file, counts the number of words in it, and writes the word count to another file. Ensure the program handles any potential file-related errors gracefully.

try:
    with open("file.txt", "r") as f:
        content = f.read()

    words = content.split()
    word_count = len(words)

    with open("count.txt", "w") as c:
        c.write(f"Word count: {word_count}")
    
    
except FileNotFoundError:
    print("File not found!")
