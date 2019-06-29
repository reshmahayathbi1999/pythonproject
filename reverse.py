Number1 = int(input())    
Reverse = 0    
while(Number1 > 0):    
    Reminder = Number1 %10    
    Reverse = (Reverse *10) + Reminder    
    Number1 = Number1 //10    
     
print(Reverse) 
