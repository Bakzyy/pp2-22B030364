# Write the definition of a Point class. Objects from this class should have a

# a method show to display the coordinates of the point
# a method move to change these coordinates
# a method dist that computes the distance between 2 points

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, x1, y1):
        self.x += x1
        self.y += y1

    def show(self):
        print(self.x, self.y)

    def dist(self, self1):
        print(math.sqrt((self1.x - self.x) ** 2 + (self1.y - self.y) ** 2))

x0 = int(input("x0="))
y0 = int(input("y0="))
x1 = int(input("x1="))
y1 = int(input("y1="))
dx = int(input("dx="))
dy = int(input("dy="))

p1 = Point(x0, y0)
p2 = Point(x1, y1)
p1.move(dx, dy)
p1.show()
p1.dist(p2)