import re
b=input()
if re.findall("[a-zA-z2-9]",b):
    print("no")
else:
    print("yes")
