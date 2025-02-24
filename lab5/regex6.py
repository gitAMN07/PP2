import re

def replace_characters(text):
    pattern = r'[ ,.]' 
    result = re.sub(pattern, ':', text) 
    return result

user_input = input("Enter a string: ")
output = replace_characters(user_input)

print("Modified string:", output)