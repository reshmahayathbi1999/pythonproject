def validateString(s):
    letter_flag = "No"
    number_flag = "No"
    for i in s:
        if i.isalpha():
            letter_flag = "Yes"
        if i.isdigit():
            number_flag = "Yes"
    return letter_flag and number_flag
s=input()
print(validateString(s))
