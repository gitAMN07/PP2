def comp(s):
    if s[::-1] == s:
        return "palindrome"
    else:
        return "not palindrome"
    
s = input()
print(comp(s))