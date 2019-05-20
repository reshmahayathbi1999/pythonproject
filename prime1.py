num1,num2=input().split()
num1=int(num1)
num2=int(num2)
for val in range(num1+1, num2):
    if val > 1: 
       for n in range(2, val): 
           if (val % n) == 0: 
               break
       else: 
           print(val,end=" ") 
