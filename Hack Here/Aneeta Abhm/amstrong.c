#include<stdio.h>
#include<conio.h>
int main()
{
    int start, end, temp, noOfDigit, num, res=0, rem, pow, i;
    printf("Enter the Interval: ");
    scanf("%d%d", &start, &end);
    printf("\nArmstrong Numbers between %d and %d:-\n", start, end);
    while(start<=end)
    {
        temp = start;
        noOfDigit=0;
        while(temp>0)
        {
            temp = temp/10;
            noOfDigit++;
        }
        num = start;
        while(num>0)
        {
            rem = num%10;
            pow = 1;
            i = 0;
            while(i<noOfDigit)
            {
                pow = pow*rem;
                i++;
            }
            res = res + pow;
            num = num/10;
        }
        if(res==start)
            printf(" %d\n", res);
        start++;
        res = 0;
    }
    getch();
    return 0;
}