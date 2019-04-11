def fact(m):
    if m==0:
        return 1
    if m==1:
        return 1
    else:
        return m*fact(m-1)
k=int(input())
print(fact(k)) 
