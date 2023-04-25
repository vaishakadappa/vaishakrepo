package vaishakproject;

import java.util.Scanner;

public class PerfectNum {
public static boolean isPerfect(int n)
{
	int sum=0;
	for(int i=1;i<=n;i++)
		if(n%i==0) {
			sum=sum+i;
			
		}
			return sum==n;
}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner s=new Scanner(System.in);
System.out.println("enter the number");
int n=s.nextInt();
boolean rs=isPerfect(n);
if(rs)
	System.out.println(n+ "perfect number");
else
	System.out.println("not a perfect number");
	}

}
