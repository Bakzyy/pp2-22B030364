#Define a class named Rectangle which inherits from Shape class from task 
# 2. Class instance can be constructed by a length and width. 
# The Rectangle class has a method which can compute the area.

class Shape:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area1(self):
        print(0)
    
class Rectangle(Shape):    
    
    def area2(self):
        
        print(self.length * self.width)
    
length = int(input())
width = int(input())


p2 = Rectangle(length, width)

p2.area1()
p2.area2()