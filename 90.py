import re
str12=input()
s=re.findall('[0-9]',str12)
for  i in s:
    print(i,end='')
