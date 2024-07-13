# Object-Oriented Programming (OOP)

# Learning Content

# -----Principles of OOP-----
# Encapsulation: Bundling the data (attributes) and methods (functions) that operate on the data into a single unit or class.
# Abstraction: Hiding the complex implementation details and showing only the essential features.
# Inheritance: Creating a new class from an existing class, inheriting its attributes and methods.
# Polymorphism: Allowing different classes to be treated as instances of the same class through a common interface.

# -----Defining classes and creating objects-----

# Syntax

class ClassName:
    def __init__(self, parameters): #  __init__() function to assign values to object properties
        # Initialize attributes
        pass
    
    def methodName(self):
        # Define method
        pass


# Example

class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says, Whoof! Whoof!"
        

# creating a Dog object
myDog = Dog("Chris", 10)
print(myDog.bark())




# -----Inheritance-----

# Syntax

class ParentClass:
    # Parent class definition
    pass

class ChildClass(ParentClass):
    # Child class definition
    pass


# Example

class Animal:
    def __init__(self, species):
        self.species = species

    def makeSound(self):
        return f"{self.species} makes some sound"
    
class Cat(Animal):
    def __init__(self, name, age):
        super().__init__("Cat")
        self.name = name
        self.age = age

    def meow(self):
        return f"{self.name} meows"
    
# creating an object of the child class
myCat = Cat("Ginger", 5)
print(myCat.meow())
print(myCat.makeSound())




# ----Polymorphism-----


# Create fifferent classes with the same method
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Drive...")

class Boat:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Sail..")

class Plane:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Fly..")


myCar = Car("Ford", "Mustang") # create car object
myBoat = Boat("Ibiza", "Touring") # create boat object
myPlane = Plane("Boeing", "747") # create plane object

# Because of polymorphism we can execute the same method for all three classes.
for x in (myCar, myBoat, myPlane):
    x.move()
        
        

# CHALLENGE: Create a simple class hierarchy (e.g., a Shape class with subclasses like Circle, Square).

# Create the parent class
class Shape:
    def __init__(self, color):
        self.color = color

    def area(self):
        pass

    def perimeter(self):
        pass


# Create SubClasses
class Circle(Shape):
    def __init__(self, color, radius):
        super().__init__(color)
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    

class Rectangle(Shape):
    def __init__(self, color, length, width):
        super().__init__(color)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
    def perimeter(self):
        return 2 * (self.length + self.width)
    

class Square(Shape):
    def __init__(self, color, side):
        super().__init__(color)
        self.side = side

    def area(self):
        return self.side ** 2
    
    def perimeter(self):
        return 4 * self.side
    

# Create Shape objects
circle = Circle("Red", 7)
square = Square("Blue", 5)
rectangle = Rectangle("Green", 10, 5)

shapes = [circle, square, rectangle]

for shape in shapes:
    print(f"{shape.__class__.__name__} - Color: {shape.color}, Area: {shape.area()}, Perimeter: {shape.perimeter()}")
    