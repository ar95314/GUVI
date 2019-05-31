n,k=map(int,input().split())
l=list(map(int,input().split()))
b=1
for i in range(0,len(l)):
	for j in range(i+1,len(l)):
		m=l[i]+l[j]
		if m==k:
			b=0
if b==0:
	print("yes")
else:
	print("no")
