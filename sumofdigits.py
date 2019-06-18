number=int(input())
tot=0
while(number>0):
    dig=number%10
    tot=tot+dig
    number=number//10
print(tot)
