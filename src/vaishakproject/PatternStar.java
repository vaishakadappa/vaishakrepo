package vaishakproject;

import java.util.Scanner;

public class PatternStar {
public static void main(String arf[])
{
	Scanner s=new Scanner(System.in);
	System.out.println("enter a number");
	int n=s.nextInt();
	int sp=n/2,st=1;
	for(int i=1;i<=n;i++)
	{
		for(int j=1;j<=sp;j++)
		{
			System.out.print(" ");

	}
		for(int j=1;j<=st;j++)
		{
			System.out.print("*");
		}
		if(i<=n/2)
		{
			sp--;
			st=st+2;
					
		}
		else
		{
			sp++;
			st=st-2;
		}
	System.out.println();
}
}}