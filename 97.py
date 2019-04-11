n=int(input())
sum12=0
while(n):
    k=n%10
    sum12=sum12*10+k
    n=n//10
print(sum12)
