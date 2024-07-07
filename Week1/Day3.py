import random

# Conditional Statements

# check if a number is positive, negative, or zero
num = float(input("Enter a number: "))

if num > 0:
    print(f"{num} is positive")
elif num == 0:
    print(f"zero")
else:
    print(f"{num} is negative")


# Loops

# For loop: print numbers from 1 to 10
for i in range(1, 11):
    print(i)

# While loop: print numbers from 1 to 10
i=1
while i <= 10:
    print(i)
    i += 1


# CHALLENGE: Write a program that asks the user to guess a number between 1 and 100. The program should give feedback if the guess is too high or too low and should keep asking until the user guesses the correct number.

# Generate a random number between 1 and 100
correct_number = random.randint(1, 100)
guess = 0

while guess != correct_number:
    guess = int(input("Guess a number between 1 and 100: "))

    if guess > correct_number:
        print("Too high! Try again.")
    elif guess < correct_number:
        print("Too low! Try again")
    else:
        print("You guessed the correct number!")

# End of Day 3