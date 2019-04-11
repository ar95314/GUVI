n12,n22=map(int,input().split())
if n12>n22:
    min1=n1
else:
    min1=n22
while(1):
    if ((min1%n12)==0) and ((min1%n22)==0):
        print(min1)
        break
    min1=min1+1
