import re
x=re.sreach(r'^(25[0-5]|2[0-4][0-9]|[0-1]?[0-9][0-9]?)$',250)
if(x):
    print("match")
else:
    print("Not match")
