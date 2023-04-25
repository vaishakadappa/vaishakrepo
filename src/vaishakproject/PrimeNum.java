package vaishakproject;
import java.util.Scanner;
public class PrimeNum {

	public static void main(String[] args) {
		Scanner s=new Scanner(System.in);
		System.out.println("enter the number");
		int a=s.nextInt();
	
	
		boolean m=true;
		for(int i=2;i<a;i++)
		if(a%i==0)
		m=false;

		if(m==true)
		System.out.println("THE NUMBER IS A PRIME NUMBER" );
		else
		System.out.println("THE NUMBER IS NOT A PRIME NUMBER");
	}
}	// TODO Auto-generated method stub