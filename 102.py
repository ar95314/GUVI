import math
def div(n12):
    if n12%2==0:
        return div(n12/2)
    else:
        return math.ceil(n12)
n1=int(input())    
print(div(n1)) 
