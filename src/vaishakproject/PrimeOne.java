package vaishakproject;
import java.util.Scanner;
public class PrimeOne {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s=new Scanner(System.in);
				System.out.println("enter a number");
int n=s.nextInt();
int count=iscount(n);
System.out.println(count);
	}
public static int iscount(int n)
{
	int count=0;
	for(int i=1;i<n;i++)
	{
		boolean rs=checkPrime(i);
	if(rs)
	{
		System.out.println(i);
	}
	count++;
	}
return count;
}
public static boolean checkPrime(int n)
{
	boolean r=true;
			for(int i=2;i<n;i++)
			{
				if(n%i==0)
					r=false;					
			}			
	return r;
	
}}
