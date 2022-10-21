#include<stdio.h>
#include<conio.h>
int main()
{
    int i;
    float mark, sum=0, avg;
    printf("Enter Marks obtained in 5 Subjects: ");
    for(i=0; i<5; i++)
    {
        scanf("%f", &mark);
        sum = sum+mark;
    }
    avg = sum/5;
    printf("\nGrade = ");
    if(avg>=91 && avg<=100)
        printf("A1");
    else if(avg>=81 && avg<91)
        printf("A2");
    else if(avg>=71 && avg<81)
        printf("B1");
    else if(avg>=61 && avg<71)
        printf("B2");
    else if(avg>=51 && avg<61)
        printf("C1");
    else if(avg>=41 && avg<51)
        printf("C2");
    else if(avg>=33 && avg<41)
        printf("D");
    else if(avg>=21 && avg<33)
        printf("E1");
    else if(avg>=0 && avg<21)
        printf("E2");
    else
        printf("Invalid!");
    getch();
    return 0;
}