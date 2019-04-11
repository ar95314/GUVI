def gcd(x,z):
    while(z):
        x,z=z,x%z
    return x 
n12,n22=map(int,input().split()) 
print(gcd(n12,n22))  
