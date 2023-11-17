# Class: Blueprint for creating new Objects
# Object/Instance: Instance of a Class, Dynamic in Nature
# Creating a Class
class Point:
    # Class Attribute : Shared across all instances of a Class
    default_color = "Red"

    # Instance Methods: __init__, draw
    # Constructor

    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Magic Method: __init__, __str__

    def __str__(self):
        return f"({self.x}, {self.y})"

    def draw(self):
        print(f"Point ({self.x}, {self.y})")
    # Comparison Magic method

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __gt__(self, other):
        return self.x > other.x and self.y > other.y

    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)

    @classmethod
    def zero(cls):
        return cls(0, 0)


# Crating Instance of a Class
point = Point(1, 2)
# Accessing Class Method
point.draw()
point.z = 5
# Checking if its an instance of Point Class
print(isinstance(point, Point))

point = Point.zero()
print(point.draw())
# Magic Methods:  They are Called automatically by python interpreter depending upon how we use object and classes.
# Eg: __init__

print(point)

# Comparing two Objects
other1 = Point(10, 20)
other2 = Point(1, 2)
# when we compare two object it compares it using their memory addresses
# if we want to compare them using their value we need to implement __eq__ magic method.
# Same goes for every but we dont have to implement it for every operator.
print(other1 == other2)
print(other1 > other2)


# Arithmetic Operation
add_other = other2 + other1
print(add_other)



