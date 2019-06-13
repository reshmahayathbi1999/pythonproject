inputnum =int(input())
count=0
array=list(map(int,input().split()))
for i in range(0,inputnum+1):
    print(array[i],i,sep=" ")
