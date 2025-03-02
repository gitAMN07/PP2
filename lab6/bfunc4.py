import math
import time
def sqrt(number, delay):
    time.sleep(delay / 1000)
    result = math.sqrt(number)
    print(f"Square root {number} after {delay} milliseconds {result}")

number = float(input("Number: "))
delay = int(input("Milliseconds: "))
sqrt(number, delay)