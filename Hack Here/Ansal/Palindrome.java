import java.util.Scanner;
public class Palindrome 
{
    public static void main(String ags[])
 {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the no: ");
        int n = sc.nextInt();
        int t = n;
        int rev=0;
        while(t != 0)
        {
            int rem = t % 10;
            rev = rev*10 + rem;
            t = t/10;
        }
        if (n==rev)
        {
            System.out.println("Palindrome");
        }
        else
        {
            System.out.println("Not Palindrome ");
        }
        sc.close();
    }
}
