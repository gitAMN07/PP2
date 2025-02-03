def prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

numbrs = list(map(int, input("Numbrs: ").split()))
prime_numbrs = list(filter(lambda x: prime(x), numbrs))
print("Prime numbrs:", prime_numbrs)