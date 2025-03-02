import math
def m_list(numbers):
    return math.prod(numbers)
input = list(map(float, input("Numbers: ").split()))

output = m_list(input)
print("Product:", output)