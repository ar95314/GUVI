import math
n,w=map(int,input().split())
l=math.sqrt(n*w)
if (l-int(l)==0.0):
    print("yes")
else:
    print("no") 
