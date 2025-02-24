import re

def find_sequences(text):
    pattern = r'\b[A-Z][a-z]+\b'
    matches = re.findall(pattern, text)

    if matches:
        print("Matching sequences:", matches)
    else:
        print("No matching sequences found.")

user_input = input("Enter a string: ")
find_sequences(user_input)