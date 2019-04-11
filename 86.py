    
str12=input()
l=[]
for i in str12:
    l.append(i)
k=set(l)
n1=len(l)
n2=len(k)
if n1-n2==0:
  print("Yes")
else:
  print("No") 
