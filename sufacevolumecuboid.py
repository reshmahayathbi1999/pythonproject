length1,width1,height1=input().split()
length1=int(length1)
width1=int(width1)
height1=int(height1)
l=length1*width1
w=width1*height1
h=height1*length1
totalsurfacearea=2*(l+w+h)
volume=length1*width1*height1
print(totalsurfacearea,volume)
