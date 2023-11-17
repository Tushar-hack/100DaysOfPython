class Animal:
    def __init__(self):
        print("Animal Constructor")
        self.age = 23

    def eat(self):
        print("eat")


# super().__init__() will call the Parent class constructor
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        print("Mammal Constructor")
        self.weight = 2

    def walk(self):
        print("walk")


class Fish(Animal):
    def swim(self):
        print("swim")


# DRY Principle : Don't Repeat Yourself

m = Mammal()
print(m.age)
print(m.weight)
print(isinstance(m, object))
print(issubclass(Mammal, object))
# Every Class in python derived from Object Class directly or Indirectly.
# Method Overriding : Extending or Replacing Method defined in the base class.
