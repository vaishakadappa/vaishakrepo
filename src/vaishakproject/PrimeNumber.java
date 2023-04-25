package vaishakproject;
import java.util.*;
public class PrimeNumber {
	public static boolean isPrimeNum(int n)
	{
		for(int i=2;i<=n/2;i++)
		{
			if(n%i==0)
				return false;
			
		}
		return true;
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		Scanner s=new Scanner(System.in);
		System.out.println("enter the number");
		int x=s.nextInt();
		boolean prime=isPrimeNum(x);
				if(prime)
					System.out.println(x +" "+ "is a prime a number");
				else
					System.out.println(x +" "+ "not a prime number");
		
	}

}
