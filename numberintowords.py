def zero():
    return "Zero"
def one():
    return "One"
def two():
    return "Two"
def three():
    return "Three"
def four():
    return "Four"
def five():
    return "Five"
def six():
    return "Six"
def seven():
    return "Seven"
def eight():
    return "Eight"
def nine():
    return "Nine"
def ten():
    return "Ten"
def default():
    return "Incorrect number"
switcher = {
    0:zero,
    1:one,
    2:two,
    3:three,
    4:four,
    5:five,
    6:six,
    7:seven,
    8:eight,
    9:nine
    }
def switch(wordsinnumber):
    return switcher.get(wordsinnumber, default)()
    
ch=int(input())
print(switch(ch))
