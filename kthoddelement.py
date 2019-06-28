num1,num2=input().split()
num1=int(num1)
num2=int(num2)
num=list(map(int,input().split()))
factor=[]
for i in num:
    if(int(i)%2!=0):
        factor.append(i)
print(factor[(num2-1)])
