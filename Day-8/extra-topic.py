# Inheritance using built-in types classes

class Text(str):
    def duplicate(self):
        return self+self


text = Text("Python")
print(text.lower())
print(text.duplicate())


class TrackableList(list):
    def append(self, object):
        print("Append called")
        super().append(object)


list = TrackableList()
list.append("1")

# Data Classes


from collections import namedtuple

Point = namedtuple("Point", ["x", "y"])
p1 = Point(x=1, y=2)
p2 = Point(x=1, y=2)
print(p1 == p2)
