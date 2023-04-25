package vaishakproject;

import java.util.Scanner;

public class PrimeTwo {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s=new Scanner(System.in);
		System.out.println("enter a number");
int n=s.nextInt();
for(int i=2;i<n;i++)
{
	if(n%i==0)
	
		System.out.println("not a prime");
		
	else
	
		System.out.println("prime num");

	
}}}
	


