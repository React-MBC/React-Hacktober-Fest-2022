import java.util.*;
public class Be_Happy
{
    public static void main(String args[])
    {
        Scanner in = new Scanner(System.in);
        System.out.println("Are you Happy or Sad");
        System.out.println("(H/S)");
        char ch=in.nextLine().charAt(0);
        if(ch=='H'||ch=='h')
        {
            System.out.println("Have a good day");
            System.out.println("Always be Happy!!");
        }
        if(ch=='S'||ch=='s')
        {
            System.out.println("Can I tell you a joke (Y/N) :");
            char c=in.nextLine().charAt(0);
            if(c=='Y'||c=='y')
            {
                
                System.out.println("What does a cloud wear under his raincoat?");
                System.out.println("Thunderwear!!");
                System.out.println("😂🤣🤣😂");
                System.out.println("Do you wanna hear more jokes(Y/N)");
                char c1=in.nextLine().charAt(0);
                int k=1;
                while(c1=='Y'||c1=='y')
                { 
                    switch(k)
                    {
                        case 1:
                        System.out.println("What time is it when the clock strikes 13?");
                        System.out.println("Time to get a new clock.");
                        
                        break;
                        case 2:
                        System.out.println("Why did the dinosaur cross the road?");
                        System.out.println("Because the chicken wasn’t born yet.");
                        
                        break;
                        case 3:
                        System.out.println("Why can’t Elsa from Frozen have a balloon?");
                        System.out.println("Because she will let it go, let it go.");
                        
                        break;
                        case 4:
                        System.out.println(" How do we know that the ocean is friendly?");
                        System.out.println("It waves.");
                        
                        break;
                        case 5:
                        System.out.println(" How do you make a lemon drop?");
                        System.out.println("Just let it fall.");
                        break;
                    }
                    if(k==5)
                    break;
                    k++;
                    System.out.println("Do you wanna hear more jokes(Y/N)");
                    c1=in.nextLine().charAt(0);
                }
            }
            else
            {
                System.out.println("Sadness flies away on the wings of time.");
                System.out.println("Bye ❤️❤️👋👋");
            }
        }in.close();
    }
}