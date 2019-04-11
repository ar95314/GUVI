import sys, string, math
def reduceN( n, b) :
	if k <= 0 : return n

	if n == 0 : return 10
	p1 = reduceN(n//10, b)*10 + n%10
	p2 = reduceN(n//10, b-1)
	if p1 < p2 :
		return p1
	else :
		return p2

n,b = input().split()
n,b = int(n),int(b)
print(reduceN(n,b))
