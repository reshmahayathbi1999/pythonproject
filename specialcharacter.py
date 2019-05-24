import re
para=input()
ans=len(para) - len( re.findall('[\w]', para) )
print(ans)
