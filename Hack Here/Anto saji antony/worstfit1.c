#include<stdio.h>
void main()
{
int i,j,mem[30],n,pro[30],m,temp,k,avail[5],t;
printf("\n enter the no. of partition of memory:");
scanf("%d",&n);
printf("\n partitions in memory:");
for(i=0;i<n;i++)
{
scanf("%d",&mem[i]);
}
printf("\n enter the no of process :");
scanf("%d",&m);
printf("\n processes are:");
for(j=0;j<m;j++)
scanf("%d",&pro[j]);
for(i=0;i<n-1;i++)
{
t=i;
for(j=i+1;j<n;j++)
{
if(mem[t]<mem[j])
{
temp=mem[j];
mem[j]=mem[t];
mem[t]=temp;
}
}
}
for(i=0;i<n;i++)
{
printf("\n processe are: %d",mem[i]);
}
for(i=0;i<m;i++)
{
for(j=0;j<n;j++)
{
if(pro[i]<=mem[j])
{
printf("\n the process %d k is placed in memory %dk",pro[i],mem[j]);
k=j;
mem[k]=0;
avail[i]=pro[i];
break;
}
}
}
for(i=0;i<m;i++)
{
if(pro[i]!=avail[i])
{
printf("\n the process %dk cannot be placed",pro[i]);
}
}
}

