import re

def match_pattern(text):
    pattern = r'^a.*b$' 
    if re.fullmatch(pattern, text):
        print(f"'{text}' matches the pattern.")
    else:
        print(f"'{text}' does NOT match the pattern.")

user_input = input("Enter a string: ")
match_pattern(user_input)