import math
num1,num2=input().split()
num1=int(num1)
num2=int(num2)
n=num1*num2
i = int(math.sqrt(n)) 
if(n == i*i):
  print("yes")
else:
  print("no")
