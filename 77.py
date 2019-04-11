k=int(input())
sum12=0
for i in range(2,k//2):
    if k%i==0:
        sum12=sum12+1
if(sum12>0):
    print("yes")
else:
    print("no")
