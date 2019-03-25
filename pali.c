#include<stdio.h>
void main()
{
int a,temp=0,n1,c;

printf("enter the number");
scanf("%d",&a);
c=a;
while(a>0)
{
n1=a%10;
temp=temp*10+n1;
a=a/10;
printf("%d\n",temp);
}
if(temp==c)
{
    printf("\npalindrome");
}
else
{
    printf("not a palindrome");
}
}
