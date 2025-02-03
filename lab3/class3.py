class Shape:
    def area(self):
        return 0

class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width
    
try:
    length = float(input("Enter the length: "))
    width = float(input("Enter the widthh: "))
    
    rectangle = Rectangle(length, width)
    print(f"Area: {rectangle.area()}")
except ValueError:
    print("Please enter valid numbers.")