import java.util.Scanner;
public class prime 
{
  public static void main(String args[])
  {
  try (Scanner sc = new Scanner(System.in)) {
    int num,a=0;
      System.out.println("enter the number ");
      num=sc.nextInt();
      for(int i=2;i<=num/2;i++)
      {
        if(num%i==0)
        {
            a=1;
            break;
        }
      }
        if(a!=0)
        {
            System.out.println(num+"is not a prime number");
        }
        else
        {
            System.out.println(num+"is a prime number");
        }
}
}
}
  
