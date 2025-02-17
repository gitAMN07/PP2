def countdown(n):
    for num in range(n, -1, -1):
        yield num

n = int(input("N: "))
print(f"Countdown from {n} to 0:")
for number in countdown(n):
    print(number)