n,q = map(int,input().split())
lis = list(map(int,input().split()))
st1 = ""
for i in range(q):
    u,v = map(int,input().split())
    ans  = min(lis[u-1:v+1])
    if(i == 0):
        st1 = st+str(ans)
    else:
        st1 = st1+"\n"+str(ans)
print(st)
