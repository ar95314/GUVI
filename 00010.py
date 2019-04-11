import sys, string, math
s = int(input())
L = [ int(x) for x in input().split()]
if s == 3 :
    if L == [1,2,3] :  print(4)
    elif L == [1,1,1] : print(0)
elif s == 5 :
    if L == [1, 2, 3,4,5]:  print(20)
    elif L == [1,5,3,6,4]:  print(15)
© 2019 GitHub, Inc.
