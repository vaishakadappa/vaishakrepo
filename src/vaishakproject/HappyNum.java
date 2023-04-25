package vaishakproject;
import java.util.Scanner;
public class HappyNum {
	public static String isHappy(int n)
	{
	while(n>9)
	{
		int sum=0;
		do
		{
			int d=n%10;
			sum=sum+d*d;
			n=n/10;
		}
		while(n!=0);
			n=sum;
		}
	
	if(n==1||n==7)
		return "happy number";
	else
		return "unhappy"	;	
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner s= new Scanner(System.in);
System.out.println("enter the number");
int x=s.nextInt();
String rs=isHappy(x);

	System.out.println(rs);


	}

}
