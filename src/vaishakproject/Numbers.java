package vaishakproject;

import java.util.Scanner;

public class Numbers {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
Scanner o =new Scanner(System.in);
System.out.println("enter the number");
int n=o.nextInt();
for(int i=1;i<=n/2;i++)
	if(n%i==0)
		System.out.println(i);
	}

}
