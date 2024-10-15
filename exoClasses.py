
class Rectangle():
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return (self.length + self.width) * 2
    
    def perimeter(self):
        return self.length * self.width

rec1 = Rectangle(4, 5)
print("the area of the rectangle is", rec1.area(), "and its perimeter is", rec1.perimeter())
