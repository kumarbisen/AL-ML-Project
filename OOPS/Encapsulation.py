## Encapsulation
## public, protected, private variables or access modifiers



### public variable 
class Person:
    def __init__(self,name,age):
        self.name = name  ## public variables
        self.age = age ## public variables

def get_name(person):
    print(person.name)

person1 = Person("vivek", 21)
get_name(person1)



## private variable

class Person:
    def __init__(self,name,age):
        self.__name = name  ## private variables
        self.__age = age ## private variables

#     def get_name(person):
#         print(person.name)

# person1 = Person("vivek", 21)
# get_name(person1)


### protected variable

class Person:
    def __init__(self,name,age,gender):
        self._name = name  ## protected variables
        self._age = age ## protected variables
        self.gender = gender
## derived class
class Employee(Person):
    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

employee = Employee("vivek", 34, "Male")
print(employee._name)

### Encapsulation with getter and setter

class Person:
    def __init__(self,name,age):
        self.__name = name
        self.__age = age
    
    ## getter method for name
    def get_name(self):
        return self.__name
    
    ## setter method for name
    def set_name(self,name):
        self.__name = name
        
    ## getter method for age
    def get_age(self):
        return self.__age
    
    ## setter method for age
    def set_age(self,age):
        if age > 0 :
            self.__age = age

        else : 
            print("Age cannot be negative")

person = Person("vivek", 32)

## Access and modify private variables using getter and setter

print(person.get_name())
print(person.get_age())

person.set_age(21)
print(person.get_age())

person.set_age(-5)
print(person.get_age())


        