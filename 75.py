str12=input()
if (len(str12)%2==0):
    k=len(str12)//2
    print(str12[:k-1]+'*'+'*'+str12[k+1:])
else:
    k=len(str12)//2
    print(str12[:k]+'*'+str12[k+1:])
