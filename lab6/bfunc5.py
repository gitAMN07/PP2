def elements_true(tup):
    return all(tup)

input = tuple(map(lambda x: x.lower() == 'true', input("Values (use 'True' or 'False'): ").split()))
print("All elements are True:", elements_true(input))