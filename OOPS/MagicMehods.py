class Person:
    def __init__(self):
        pass

person = Person()



## Basics Methods
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

people = People("vivek", 21)
# print(people)



## Basics Methods
class People:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name}, {self.age} years old"
    
    def __repr__(self):
        return f"person(name= {self.name}, age = {self.age})"

people = People("vivek", 21)
print(people)
print(repr(people))
