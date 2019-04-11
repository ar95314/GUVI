m=int(input())
k=round(pow(n,0.5))
li=[]
for i in range(0,k):
    t=pow(2,i)
    li.append(t)
if m in li:
    print("yes")
else:
    print("no")
