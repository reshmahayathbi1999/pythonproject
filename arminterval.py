num1,num2=input().split()
num1=int(num1)
num2=int(num2)
for num in range(num1,num2):
    sum = 0
    temp = num
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if num == sum:
        print(num,end=" ")
