s=input()
m=len(s)
l=[]
for i in range(m):
    if int(s[i])%2!=0:
       l.append(s[i])
k=len(l)        
for i in range(k-1):
    print(l[i],end=' ')
print(l[k-1])  
