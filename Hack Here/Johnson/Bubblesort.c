#include<stdio.h>
void main()
{
int A[20],n,i,j,temp;
printf("Enter the limit of array: ");
scanf("%d",&n);
for(i=0;i<n;i++)
{
printf("Enter the elements in the array: ");
scanf("%d",&A[i]);
}
for(i=0;i<n-1;i++)
{
for(j=0;j<n-i-1;j++)
{
if(A[j]>A[j+1])
{
temp=A[j];
A[j]=A[j+1];
A[j+1]=temp;
}
}
}
printf("The Sorted Array is:\n");
for(i=0;i<n;i++)
{
printf("%d\t",A[i]);
}
}
