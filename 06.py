lst1=[]
lst2=[]
class check:
	def ifisomorphic(self,k,m):
		for i in k:
			lst1.append(i)
		for i in m:
			lst2.append(i)
		len12=len(set(lst1))
		len22=len(set(lst2))
		if len12==len22:
			print("yes")
		else:
			print("no")
n,m=map(str,input().split())
call=check()
call.ifisomorphic(n,m)
