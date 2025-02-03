class Shape:
    def area(self):
        return 0

class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length ** 2

try:
    length = float(input("Enter the length: "))
    square = Square(length)
    print(f"Area: {square.area()}")
except ValueError:
    print("Please enter a valid number.")
