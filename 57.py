k,m=map(int,input().split())
sum1=0
z=[int(i) for i in input().split()]
for i in range(0,n):
    if(m==z[i]):
        sum1=sum1+1
print(sum1)       
