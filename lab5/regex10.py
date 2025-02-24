import re

def camel_to_snake(camel_str):
    snake_str = re.sub(r'([a-z])([A-Z])', r'\1_\2', camel_str).lower()
    return snake_str

user_input = input("Enter a camelCase string: ")
output = camel_to_snake(user_input)

print("Snake case string:", output)