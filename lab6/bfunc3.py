def polindrome(text):
    txt = ''.join(filter(str.isalnum, text)).lower() 
    return txt == txt[::-1] 

input = input("StrIng: ")

if polindrome(input):
    print("Is a polindrome.")
else:
    print("NOT a polindrome.")