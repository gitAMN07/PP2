def trapezoid_area(b1, b2, h):
    return 0.5 * (b1 + b2) * h

b1 = float(input("Length of the fist base: "))
b2 = float(input("Length of the second base: "))
h = float(input("Height: "))

area = trapezoid_area(b1, b2, h)
print(f"The area of the trapezoid: {area:.2f}")