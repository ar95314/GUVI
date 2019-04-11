d = input()
d = list(s)
for i in range(0,len(d),2):
    d[i], d[i+1] = d[i+1], d[i]  
print( ''.join(d))
