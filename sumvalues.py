n,k=input().split()
n=int(n)
k=int(k)
values=input().split()
sum=0
counter=0
while(counter<k):
    sum=sum+int(values[counter])
    counter+=1
print(sum)
