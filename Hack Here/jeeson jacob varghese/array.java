import java.util.Scanner;
public class array
{
public static void main(String args[])
 {
 try (Scanner = new Scanner(System.in)) {
    System.out.println("enter the size of array");
     int n=sc.nextInt();
     System.out .println("enter the number");
     int a[]=new int[n];
     for (int i=0;i<n;i++)
     a[i]=sc.nextInt();
     int temp;
    for (int i=0;i<n;i++)
    {
    for (int j=0;j<i+1;j++)
    {
        if(a[i]<a[j])
        {
            temp=a[i];
            a[i]=a[j];
            a[j]=temp;
        }
    }
    }
    System.out.println("sorted array is :");
    for(int i=0;i<n;i++)
    {
        System.out.println(a[i]);
    }
}
}
}