# inheritance (single inheritance): When a class inherits from one base class
 ## parent class
class Car:
    def __init__(self,windows,doors,enginetype):
      self.windows =  windows
      self.doors = doors
      self.enginetype = enginetype
    
    def drive(self):
       print(f"The person is drive the {self.enginetype} car")


class tesla(Car):
    def __init__(self,window,doors, enginetype, is_selfdriving):
      super().__init__(window,doors,enginetype)
      self.is_selfdriving= is_selfdriving

    def selfdriving(self):
        print(f"tesla supports selfdriving : {self.is_selfdriving}")

      

tesla1 =tesla(4,2,"petrol",True)
tesla1.selfdriving()

tesla1.drive()




### Multiple inheritance : When a class inherits from more than one base class.
## Base class1

class Animal:
    def __init__(self,name):
      self.name = name
    def speak(self):
       print("Subclass must impliment this method")
## Base class2

class Pet:
   def __init__(self,owner):
      self.owner = owner


## derived class

class Dog(Animal,Pet):
    def __init__(self, name,owner):
      Animal.__init__(self,name)
      Pet.__init__(self,owner)

    def speak(self):
       return f"{self.name} say woof"

dog = Dog("bumpy","vivek")
print(dog.speak())
    
     
      



      
      
      


 