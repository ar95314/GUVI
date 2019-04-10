#include <stdio.h>
int max(int array[100],int a);
int main(void) 
{
	int array[100];
	int i,result,a;
	printf("no of elements in the array");
	scanf("%d",&a);
	printf("\narray\n");
	for(i=0;i<a;i++)
	{
	scanf("%d",&array[i]);
	printf("%d ",array[i]);
	}
	result=max(array,a);
	printf("\n%d",result);
	return 0;
}
int max(int array[100],int a)
{
	int i,mx=array[0];
	for(i=1;i<a;i++)
	{
	scanf("%d",&array[i]);
	if(array[i]>mx)
	{
		mx=array[i];
	}
	}
	return (mx);
}	
