m=int(input())
li=[]
for i in input().split():
    li.append(int(i))
li.sort()
print(li[0],end=' ')
print(li[-1],end='')
