package vaishakproject;
import java.util.Scanner;
public class PatternString {

	public static void main(String[] args) {
		
		Scanner s=new Scanner(System.in);
		System.out.println("enter the number");
		String st=s.next();
		int n=s.nextInt();
		for(int i=1;i<=n;i++)
		{
			for(int j=0;j<i;j++)
			{
			 System.out.print(st.charAt(j) + "");
		
			}
			System.out.println();
		}
		
		
		
		
		
		
	}

}
