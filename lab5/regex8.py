import re

def split_at_uppercase(text):
    words = re.findall(r'[A-Z][a-z]*', text)
    return words

user_input = input("Enter a string: ")
output = split_at_uppercase(user_input)

print("Splt words:", output)