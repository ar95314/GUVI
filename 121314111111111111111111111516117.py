import collections

n1 = int(input())
a = []
b = input().split()
for i in range(0,n1):
	a.append(b[i])

results = collections.Counter(a)
c = []
#print(results)
for i in results:
	if(results[i]>1):
		c.append(i)
		break
#c = sorted(c)
if not c:
	print("unique")
else:
	#print(" ".join(c[0]))
	#print(c)
	seen = set()
	for i in a:
		if i in seen:
			print(i)
			break
		else:
			seen.add(i)
