a,r,n=map(str,input().split())
g=[]
for i in range(int(a),int(r)+1):
	g.append(str(i))
c=0
for i in g:
	if n in i:
		c+=1
print(c)
