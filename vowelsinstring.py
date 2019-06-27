string1=input()
vowels = ["a", "e", "i", "o", "u"]
if any(char in vowels for char in string1):
    print('yes')
else:
    print('no')
