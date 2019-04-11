#include <stdio.h>

int main(void) {
	char string[150];
	int n,i;
	scanf("%s",&string);
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		printf("%s",string);
		printf("\n");
	}
	return 0;
}
