number=int(input())
for i in repr(number):
    if i.isdigit():
        if(int(i)%2!=0):
            print(i,end=" ")
