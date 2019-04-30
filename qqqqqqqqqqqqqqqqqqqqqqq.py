amu1=list(map(int,raw_input().split()))
abi=list(map(int,raw_input().split()))
q=[]
for i in range(amu1[1]):
  c=list(map(int,raw_input().split()))
  m=abi[(c[0]-1)]^abi[(c[0])]
  for j in range(c[0]+1,c[1]):
    m=m^abi[j]
  q.append(m)
for i in range(len(q)):
  print(q[i])
