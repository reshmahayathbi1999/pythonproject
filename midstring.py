string=input()
len1=len(string)
mid=int((len1- 1)/2)
if(len1%2!=0):
    print(string[0:mid]+'*'+string[mid+1:])
else:
    print(string[0:mid]+'**'+string[mid+2:])
    
