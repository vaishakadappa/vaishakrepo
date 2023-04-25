package vaishakproject;

import java.util.Scanner;

public class Reverse {

	public static void main(String[] args) {

		Scanner s = new Scanner(System.in);
		System.out.println("enter the num:");
		// int n=s.nextInt();
int n=1000986;
		String str = s.nextLine();
//String str = Integer.toString(n);
//String str="vaishak";
		char[] ch = str.toCharArray();

		for (int i = ch.length - 1; i >= 0; i--) {
System.out.print(ch[i]);
		}
	}
}