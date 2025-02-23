class PiggyBank:
    def __init__(self):
        self.__balance=0
    def add_money(self,ammount):
        if ammount>0:
            self.__balance+=ammount
        else:
            print("You can't add negative money")
    def check_balance(self):
        return self.__balance

ammount=PiggyBank()
ammount.add_money(100)
print(ammount.check_balance())


##------------------------   Q-2   ----------------------------

print("-----------------------------------------")

class Car:
    def __init__(self,make):
        self.__make=make
    def get_make(self):
        return self.__make
    def set_make(self,n_make):
        self.__make=n_make

car= Car("Toyota")
print(car.get_make())

car.set_make("Honda")
print(car.get_make())

##--------------------------- Q-3 ---------------------------

print("------------------------------------------------------")

class Vehicle:
    def __init__(self,brand):
        self.brand=brand
    def drive(self):
        print("The vehicle is moving")

class Car(Vehicle):
    def __init__(self,brand,model):
        super().__init__(brand)
        self.model=model
    def honk(self):
        print("Deep! Deep")

car= Car("Toyota","corola")
car.drive()
car.honk()



##------------------------------- Q-4 -------------------------------------
print("------------------------------------------------------")

class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Woof!")

animal = Animal()
animal.sound()  

dog = Dog()
dog.sound()  

##------------------------------- Q-5 -------------------------------------
print("------------------------------------------------------")

class Animal:
    def sound(self):
        raise NotImplementedError("Subclasses must override sound() method")

class Dog(Animal):
    def sound(self):
        return "Woof!"

class Cat(Animal):
    def sound(self):
        return "Meow!"

animals = [Dog(), Cat(), Dog(), Cat()]

for animal in animals:
    print(animal.sound())

##------------------------------- Q-6 -------------------------------------
print("------------------------------------------------------")

from abc import ABC, abstractmethod

class Animal(ABC):
    def _init_(self, name):
        self.name = name
    
    @abstractmethod
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

dog = Dog()
cat = Cat()

dog.make_sound() 
cat.make_sound() 