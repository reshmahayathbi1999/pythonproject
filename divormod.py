num1,oper,num2 =input().split()
num1=int(num1)
num2=int(num2)
if oper == '/':
    print(round(num1 / num2))
elif oper == '%':
    print((num1 % num2))
