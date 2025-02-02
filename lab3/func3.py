def solve(numheads, numlegs):
    y = (numlegs - 2 * numheads) // 2
    x = numheads - y
    
    if x >= 0 and y >= 0 and 2 * x + 4 * y == numlegs:
        return x, y
    else:
        return "No valid solution"

numheads = int(input("Heads: "))
numlegs = int(input("Legs: "))
print(solve(numheads, numlegs))