amu1=raw_input().split()
amu1=list(map(int,amu1))
s=raw_input().split()
s=list(map(int,s))
c=[]
for i in range(amu1[1]):
  d=raw_input().split()
  c.append(list(map(int,d)))
for i in range(amu1[1]):
  print(min(s[(c[i][0]-1):c[i][1]]))
