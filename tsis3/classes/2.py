# Define a class named Shape and its subclass Square. 
# The Square class has an init function which takes a length as argument. 
# Both classes have a area function which can print the area of the shape where Shape's area is 0 by default.

class Shape:
    
    def __init__(self, length):
        
        self.length = length
    
    def area1(self):
        
        print(0)
    
class Square(Shape):
    
    def area2(self):
        
        print(self.length ** 2)
    
length = int(input())

p2 = Square(length)

p2.area1()
p2.area2()