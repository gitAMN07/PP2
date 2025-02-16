def square_generator(N):
    for num in range(1, N + 1):
        yield num ** 2 

N = int(input("N: "))
print(f"Squares up to {N}:")
for square in square_generator(N):
    print(square)