a=int(input())
b=1
m=2
while m<=a:
    if 2**b==a:
        b=0
        break
    else:
        m=2**b
        b=b+1
if(b!=0):
    b=b-2
    q=a-2**b
    print(q)
else:
    print(0)
