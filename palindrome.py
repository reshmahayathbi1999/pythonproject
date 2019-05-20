num = input()
try:
    if num ==num[::-1]:
        print('yes')
    else:
        print('no')
except:
    print("That's not a valid number, Try Again !")
