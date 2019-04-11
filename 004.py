s12,s22=input().split()
s=0
if len(s12)>len(s22):
  s12,s22=s22,s12
i=0
while i<len(s12):
  s+=(ord(s22[i])-ord(s12[i]))
  i+=1
for i in range(i,len(s22)):
  s+=ord(s22[i])-ord('a')+1
print(s)
