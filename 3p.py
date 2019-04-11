s=int(input())
rev=0
k=0
while(s):
    k=s%10
    rev=rev*10+k
    s=s//10
print(rev) 
