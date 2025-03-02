def count(text):
    up_count = sum(map(str.isupper, text))
    low_count = sum(map(str.islower, text))
    print("Uppercase:", up_count)
    print("Lwercase:", low_count)

user_input = input("Strng: ")
count(user_input)