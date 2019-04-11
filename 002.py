def reduceN(m,k):
    if k<=0: return m
    if m==0: return 10
    p1=reduceN(m//10,k)*10+m%10
    p2=reduceN(m//10,k-1)
    if p1<p2:
        return p1
    else:
        return p2
m,k=input().split()
m,k=int(m),int(k)
print(reduceN(m,k)
