n,k=map(int,input().split())
l1=[int(i) for i in input().split()]
sum1=0
for i in range(0,len(l1)):
    if((l1[i]%2)!=0):
        sum1=sum1+1
        if sum1==k:
            print(l1[i])
    else:
        pass
