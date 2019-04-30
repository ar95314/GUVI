#include <stdio.h>
void main()
{
    char str1[50];
    scanf("%[^\n]s",str1);
    int l=strlen(str1),i;
    int hash[l+1];
    for(i=0;i<l+1;i++){
        hash[i]=0;
    }
    hash[0]=1;
    hash[1]=1;
    for(i=2;i<=l;i++){
        if(str1[i-1]>'0'){
            hash[i]=hash[i-1];
        }
        if((str1[i-2]=='2'&&str1[i-1]<'7')||str[i-2]<'2'){
            hash[i]=hash[i]+hash[i-2];
        }
       
    }
    printf("%d",hash[l]);
 
}
