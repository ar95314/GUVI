s12,s22=input().split()
n1=len(s12)
n2=len(s22)
if n2>n1:
    i=0
    while i<n1 and s12[i]==s22[i]:
        i+=1
    print(n2-i)
elif n2==n1:
    i=0
    while i<n2 and s12[i]==s22[i]:
        i+=1
    print(n2-i)
else:
    i=0
    while i<n2 and s12[i]==s22[i]:
        i+=1
    s31=s12[i:]
    s32=s22[i:]
    l=list(s31)
    k=0
    for c in s32:
        if c in l:
            k+=1
            l.remove(c)
    print(n1-i-k)
