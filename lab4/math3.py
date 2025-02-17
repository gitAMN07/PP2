import math

def regular_polygon_area(n, side_length):
    return (n * side_length ** 2) / (4 * math.tan(math.pi / n))

n = int(input("Enter the number of sides: "))
side_length = float(input("Enter the length of a side: "))

if n < 3:
    print("A polygon must have at least 3 sides.")
else:
    area = regular_polygon_area(n, side_length)
    print(f"The area of the regular polygon: {area:.2f}")