num = input()
try:
    if num ==num[::-1]:
        print('The given number is PALINDROME')
    else:
        print('The given number is NOT a palindrome')
except:
    print("That's not a valid number, Try Again !")
