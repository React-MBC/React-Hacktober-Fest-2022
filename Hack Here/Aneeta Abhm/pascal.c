#include<stdio.h>
#include<conio.h>
int main()
{
    int row, col, i=1, j=0, arr[5], arrTemp[5];
    arr[0] = 1;
    arr[1] = 1;
    for(row=0; row<5; row++)
    {
        for(col=4; col>row; col--)
            printf(" ");
        for(col=0; col<=row; col++)
        {
            if(row==0)
                printf("1");
            else
            {
                if(col==0 || col==row)
                    printf("1 ");
                else
                {
                    arrTemp[i] = arr[j]+arr[j+1];
                    printf("%d ", arrTemp[i]);
                    i++;
                    j++;
                }
            }
        }
        printf("\n");
        arrTemp[i] = 1;
        if(row>1)
        {
            j=0;
            arr[j]=1;
            for(j=1, i=1; j<=row; j++, i++)
                arr[j] = arrTemp[i];
            i=1;
            j=0;
        }
    }
    getch();
    return 0;
}