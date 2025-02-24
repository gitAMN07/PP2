import re

def insert_spaces(text):
    spaced_text = re.sub(r'([a-z])([A-Z])', r'\1 \2', text)
    return spaced_text

user_input = input("Enter a CamelCase string: ")
output = insert_spaces(user_input)

print("Modified string:", output)