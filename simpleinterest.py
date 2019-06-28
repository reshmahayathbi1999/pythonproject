import math
num1,num2,num3=input().split()
num1=int(num1)
num2=int(num2)
num3=int(num3)
interest=(num1*num2*num3)/100
print(math.floor(interest))
