str12=input()
l=[]
for i in range(0,len(str12)):
    l.append(ord(str12[i]))
l.sort()
for i in l:
    print(chr(i),end='')
