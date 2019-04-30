import sys, string, math
n1,k = input().split()
n1,k = int(n1), int(k)
L = [ int(x) for x in input().split()]
for i in range(0,k) :
     a,b = input().split()
     a,b = int(a), int(b)
     print(min(L[a-1:b]))
