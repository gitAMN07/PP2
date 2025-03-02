import string
def generate_files():
    for letter in string.ascii_uppercase:
        name = f"{letter}.txt"
        with open(name, "w", encoding="utf-8") as file:
            file.write(f"It is {name}\n")
        print(f"Created: {name}")

generate_files()