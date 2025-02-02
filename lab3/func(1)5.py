def print_permutations(s, a=""):
    if len(s) == 0:
        print(a)
        return
    
    for i in range(len(s)):
        char = s[i]
        remaining = s[:i] + s[i+1:]
        print_permutations(remaining, a + char)

print_permutations(input("Enter: "))
