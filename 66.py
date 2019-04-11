k=int(input())
sum11=0
for i in range(2,k//2):
    if k%i==0:
        sum11=sum11+1
if(sum11>0):
    print("no")
else:
    print("yes")
