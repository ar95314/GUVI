s11, s12 = input().split()
c = 0
for i in range(len(s11)) :
    if s11[i] != s12[i] :
        c += 1
if c == 1 : print('yes')
else :      print('no')
