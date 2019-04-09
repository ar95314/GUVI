#include <stdio.h>

int main(void) {
	// your code goes here
	int full,half,i,sum=0;
	scanf("%d%d",&full,&half);
	
		for(full=1;full<=half;full++)
		{
			sum=sum+full;
		
		}
		printf("%d",sum);
	return 0;
}
