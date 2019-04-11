num=int(input())
stepss=list(map(int,input().split()))
tota=0
for i in range(1,len(stepss)):
	     for j in range(0,i):  
		           if(stepss[j]<stepss[i]):
			                 tota+=stepss[j]
print(tota)
