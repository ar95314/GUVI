import syst, string, math
n,u = input().split()
n,u = int(n), int(a)
L = [ int(x) for x in input().split()]
for i in range(0,u) :
    a,b = input().split()
    a,b = int(a), int(b)
    print(sum(L[a-1:b]))
