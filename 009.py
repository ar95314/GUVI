# kirthika
import sys, string, math
def hcf(L) :
	hcf1 = 1
	for i in range(2,min(L)+1) :
		if all([x%i==0 for x in L]) :
			hcf1 = i
	return hcf1
 
n1,k = input().split()
n1,k = int(n1), int(k)
L = [ int(x) for x in input().split()]
for i in range(0,k) :
	a,b = input().split()
	a,b = int(a), int(b)
	hcf1 = hcf(L[a-1:b])
	print(hcf1)
