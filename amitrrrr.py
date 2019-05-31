l,r,n=map(str,input().split())
g=[]
for i in range(int(l),int(r)+1):
	g.append(str(i))
d=0
for i in g:
	if n in i:
		d+=1
print(d)
