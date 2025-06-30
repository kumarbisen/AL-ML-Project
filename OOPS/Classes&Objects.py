### class
class Car:
    pass
audi = Car()
bmw = Car()

print(type(audi))


### insatance variable and Method

audi.color = "red"
print(audi.color)

class Dog:
    ### constructor
    def __init__(self,name, age):
        self.name = name
        self.age = age 
 
    ### create objects
dog1 =Dog("buddy",3)
print(dog1.age,dog1.name)

### Define a class with instance methods

class dog:
    def __init__(self,name,age):
        ### objects are like properties of attributes
        self.name = name
        self.age = age

        ### methods are like some work done by class
    def bark(self):
        print(f"{self.name} says woof" )
    

dog1 = dog("buddy",5)
dog2 = dog("Lucy",4)
dog1.bark()
dog2.bark()


## Modeling a Bank Account Example

## Define a class for bank account
class BankAccount:
    def __init__(self,owner,balance=0):
        self.owner =  owner
        self.balance = balance

    def deposit(self,amount):
        amount += self.balance
        print(f"{amount} is deposited and New balance is {self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount
            print(f"{amount} is withdrawn and New balance is {self.balance}")
    def get_balance(self):
        return self.balance
    
account = BankAccount("Vivek", 500)
print(account.balance)
account.withdraw(400)
print(account.get_balance())

