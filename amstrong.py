a=int(input("Enter the number"))
sum=0
temp=a
while temp>0:
   digit=temp%10
   sum=sum+digit**3
   if a==sum:
       print(a,"Amstrong")
   else:
       print(a,"Not Amstrong")
   
