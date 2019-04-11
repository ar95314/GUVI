import sys, string, math
x,y = map(int,input().split())
k = 0
for i in range(x,y+1) :
    for j in range(2,i) :
        if i%j == 0 :
            break
    else :
        k += 1
print(k)
