import java.util.Scanner;

public class dey {

    public static void main(String Args[])
    { 
        Scanner sc=new Scanner(System.in);
        System.out.println("enter the line"); 
        String str=sc.nextLine();
        System.out.println("enter the character");
        char ch=sc.nextLine().charAt(0);
        int count=0;
        for(int i=0;i<str.length();i++)
        {
            if(str.charAt(i)==ch)
            {
                count++;
            }
            } System.out.println("count is"+count);
    }
}