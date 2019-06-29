def isogram(word): 
    clean_word = word.lower() 
    listt = []   
    for letter in clean_word: 
        if letter.isalpha(): 
            if letter in listt: 
                return "No"
            listt.append(letter)   
    return "Yes"
word=input()
if __name__ == '__main__': 
    print(isogram(word))
