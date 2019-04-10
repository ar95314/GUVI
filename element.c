#include <stdio.h>
int main()
{
    int a,i,arr[n],s=0,median;
    scanf("%d",&a);
    for(i=0;i<a;i++)
    {
      scanf("%d",&arr[i]);
    }
    for(i=0;i<a;i++)
    {
    s=s+arr[i];
    }
    median=s/a;
    printf("%d",median);
    return 0;
}
