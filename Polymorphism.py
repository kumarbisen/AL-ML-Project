 ## Polymorphism is typically achieved through method overriding and interfaces
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

## Polymorphism with Function and Methods


class Shape:
    def area(self):
        return "The area of the figure"