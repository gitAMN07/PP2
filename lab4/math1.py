import math

def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)

degrees = float(input("Degrees: "))
radians = degrees_to_radians(degrees)
print(f"{degrees} degrees is equal to {radians:.6f} radians")