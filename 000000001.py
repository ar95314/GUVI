mn=int(input())
list=input().split()
l=[]
for i in range(0,mn):
   if i==int(list[i]):
      l.append(str(i))
if l==[]:
   l.append(str(-1))
l=" ".join(l)
print(l)
