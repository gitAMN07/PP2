import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self):
        self.x, self.y = map(float, input("New coordinates: ").split())

    def dist(self, other_point):
        return math.sqrt((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2)

x1, y1 = map(float, input("Enter coordinates for first point: ").split())
p1 = Point(x1, y1)

x2, y2 = map(float, input("Enter coordinates for second point: ").split())
p2 = Point(x2, y2)

print("First point:", end=" "); p1.show()
print("Second point:", end=" "); p2.show()
print(f"Distance between points: {p1.dist(p2):.2f}")
p1.move()
print("Updated first point:", end=" "); p1.show()
