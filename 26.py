n=int(input())
lis=list(map(int,input().split()))
lis.sort()
for i in range(len(lis)):
	if i==len(lis)-1:
		print(li[i],end="")
	else:
		print(li[i],end=" ")
