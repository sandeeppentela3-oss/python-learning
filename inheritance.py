# Parent class
class Animal:
    def eat(self):
        print("Animal is eating")

# Child class
class Dog(Animal):
    def bark(self):
        print("Dog is barking")

# Creating an object
d = Dog()

d.eat()
d.bark()