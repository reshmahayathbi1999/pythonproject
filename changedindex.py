Number = int(input())
NumList =list(map(int,input().split()))
for i in range (Number):
    for j in range(i + 1, Number):
        if(NumList[i] > NumList[j]):
            print(NumList[i-1]) 
            break
            
