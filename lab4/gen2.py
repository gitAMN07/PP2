def even_generator(n):
    for num in range(0, n + 1, 2):
        yield num

n = int(input("N: "))
print("Even numbers:", ", ".join(map(str, even_generator(n))))