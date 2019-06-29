import math
def lcm(n1,n2):
  gcd = math.gcd(n1,n2)
  result = (n1*n2)/gcd
  return result

n1,n2=input().split()  
n1 = int(n1)
n2 = int(n2)
 
value = lcm(n1,n2)
print(round(value))
