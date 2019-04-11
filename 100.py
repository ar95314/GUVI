s=int(input())
prod=1
k=0
while(s):
    k=s%10
    prod=prod*k
    s=s//10
print(prod)
