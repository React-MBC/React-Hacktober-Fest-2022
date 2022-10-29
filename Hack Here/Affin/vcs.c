# include<stdio.h>
void main()
{
int i,v=0,c=0,s=0;
char str[20];
printf("Enter the String(ending with $): ");
scanf("%s",str);
for(i=0;str[i]!='$';i++)
{
if(str[i]=='a' || str[i]=='e' || str[i]=='i' || str[i]=='o' || str[i]=='u' || str[i]=='A' || str[i]=='E' || str[i]=='I' || str[i]=='O' ||  str[i]=='U')
{
++v;
}
if((str[i]>='a' && str[i]<='z' && (str[i]!='a' && str[i]!='e' && str[i]!='i' && str[i]!='o' && str[i]!='u'  ))||(str[i]>='A' && str[i]<='Z' && (str[i]!='A' && str[i]!='E' && str[i]!='I' && str[i]!='O' &&  str[i]!='U')))
{
++c;
}
if(str[i]==' ')
{
++s;
}
}
printf("No:of Vowels=%d\n",v);
printf("No:of Consonants=%d\n",c);
printf("No:of White Spaces=%d\n",s);
}
