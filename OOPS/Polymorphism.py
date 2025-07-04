 ## Polymorphism is typically achieved through method overriding and interfaces

## Method overiding
class Animal:
    def speak(self):
        return "animal sound "
class Dog(Animal):
    def speak(self):
        return "woof!"
    
class Cat(Animal):
    def speak(self):
        return "meow!"

## function that demostrates polymorphism
def animal_speak(animal):
    print(animal.speak())


dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())
animal_speak(dog)





## polymorphism with functions and methods 
class Shape:
    def area():
        return "this gives you the area of the figure"

class Rectangle(Shape):
    def __init__(self,height, width):
       self.height = height
       self.width = width
    def area(self):
        return self.height * self.width
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius= radius

    def area(self):
        return 3.14 * self.radius * self.radius

## function that demonstrate polymorphism
def print_area(shape):
    print(f"The area {shape} is {shape.area()}")


rect = Rectangle(3,4)
print_area(rect)



## polymorphism with Abstract base classes
from abc import ABC,abstractmethod

# Define an abstact class
class Vehicle(ABC):
    @abstractmethod

    def start_engine(self):
       pass
## Derived class 1

class Car(Vehicle):
    def start_engine(self):
        return "car engines started"

# Derived class 2
class Motorcycle(Vehicle):
    def start_engine(self):
        return "Motorcycle engines started"
# function that demonstrate polymorphism
def start_vehicle(vehicle):
    print(vehicle.start_engine())


car = Car()
moto = Motorcycle()
start_vehicle(car)
start_vehicle(moto)


       