import re

x=re.search(r'^[\w][.\w]*@[\w][.\w][.\w]+$',"abcd.pqr@1gmal.co.in")

if(x):
    print("match")
else:
    print("not match")

