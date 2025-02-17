def parallelogram_area(base, height):
    return base * height

base = float(input("Base lenghh of the parallelogram: "))
height = float(input("Height of the parallelogram: "))
area = parallelogram_area(base, height)
print(f"The area of the parallelpgram: {area:.2f}")