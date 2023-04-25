package vaishakproject;

import java.util.Scanner;

public class ReverseNum {

	public static void main(String[] args) {
Scanner s= new Scanner(System.in);
System.out.println("enter the num");
int num = s.nextInt();

int rev=0;
while(num!=0) {
	rev=rev*10 + num%10;
	num=num/10;
}
System.out.println("reverse number is"+ rev);
	}

}
