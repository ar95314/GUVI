m=int(input())
l=[int(i) for i in input().split()]
for i in range(0,m):
    if((i+1)!=l[i]):
        print(i)
        break
