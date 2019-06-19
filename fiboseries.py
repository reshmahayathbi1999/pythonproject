Number = int(input())
i =1
First_Value =0
Second_Value =1
while(i < Number+1):
           if(i <=1):
                      Next = i
           else:
                      Next = First_Value + Second_Value
                      First_Value = Second_Value
                      Second_Value = Next
           print(Next,end=" ")
           i = i + 1
