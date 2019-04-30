N=int(raw_input())
S1=str(N)
c=0
for i in range(0,len(S1)):
    if(int(S1[i:i+2])<26 and len(str(int(S1[i:i+2])))==2):
        c=c+1
if c==2:
    print(c+c//2)
else:
    print(c+c//2+1)
