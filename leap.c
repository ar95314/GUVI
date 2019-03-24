#include <stdio.h>

int main()
{
    int ye;
    scanf("%d",&ye);

    if(ye%4 == 0)
    {
        if( ye%100 == 0)
        {
            if ( y%400 == 0)
                printf("%d is a leap year.",ye);
            else
                printf("%d is not a leap year.",ye);
        }
        else
            printf("%d is a leap year.",ye );
    }
    else
        printf("%d is not a leap year.",ye);
    
    return 0;
}
