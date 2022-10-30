include <stdio.h>
int main()
{
    int n,sum=0,r,armstrong;
    printf("Enter n:");
    scanf("%d",&n);
    armstrong=n;
    while(n!=0)
    {
        r=n%10;
        sum=sum+r*r*r;
        n=n/10;
    }
    if(armstrong==sum)
    printf("Armstrong number");
    else
    printf("Not an armstrong number");
}
