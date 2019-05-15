value=input()
if((value=='a') or (value=='e') or (value=='i') or (value=='o') or (value=='u')):
    print("Vowel")
elif((value!='a' or value!='e' or value!='i' or value!='o' or value!='u') and (value>'a' and value<='z')):
    print("Consonant")
else:
    print("invalid")
