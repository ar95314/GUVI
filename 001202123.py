lst1=[]
class findno:
	def appeares(self,a,lst):
		lst.sort()
		for i in range(0,a):
			if i!=a-1:
				if lst[i]==lst[i+1]:
					if lst[i] not in lst1:
						lst1.append(lst[i])
		for i in range(len(lst)):
			if lst[i] not in lst1:
				print(lst[i])
a=int(input())
lst=list(map(int,input().split()))
call=findno()
call.appeares(a,lst)
