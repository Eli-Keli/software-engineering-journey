# Decorators and Generators
"""
Objectives
Understand and use decorators in Python.
Learn about generators and how they can be used to create iterators.

Learning Content
Decorators

What is a Decorator?
A decorator is a function that takes another function and extends its behavior without explicitly modifying it.
"""
# Example
def myDecorator(func):
    def wrapper():
        print("First")
        func()
        print("Continue")
    
    return wrapper

@myDecorator
def example():
    print("Hello")

example()



"""
Generators

What is a Generator?
Generators are a simple way to create iterators using a function that yields values one at a time.
"""

# Example
def count_up_to(max):
    count = 0

    while count <= max:
        yield count
        count += 1

counter = count_up_to(5)

for count in counter:
    print(count) # Output: 1 2 3 4 5



"""
CHALLENGE
Write a decorator that logs the execution time of a function and a generator that yields prime numbers.
"""

# Decorator
import time

def execution_time(func):
    def wrapper(*args, **Kwargs):
        start_time = time.time()
        result = func(*args, **Kwargs)
        end_time = time.time()

        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@execution_time
def example_function():
    for _ in range(1000000):
        pass

example_function()


# Generator

def prime_numbers():

    num = 2
    
    while True:
        is_prime = all(num % i != 0 for i in range(2, int(num ** 0.5) + 1))

        if is_prime:
            yield num
            num += 1

primes = prime_numbers()

for _ in range(10):
    print(next(primes))