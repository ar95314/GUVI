import re
k=input()
if (re.findall('[a-zA-Z]',k) )and( re.findall('[0-9]',k)):
    print("Yes")
else: 
    print("No")
