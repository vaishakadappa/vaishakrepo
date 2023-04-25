package vaishakproject;

public class Palindrome {
	static void isPalindrome(int n)
	{
	 int rev=0,temp=n;
	 while(n!=0)
	 {
		 int r=n%10;
		 rev=rev*10+r;
		 n=n/10;
	
	 }

	}
	
	public static void main(String[] args) {
		// TODO Auto-generated method stub
	for(int i=101;i<=999;i++)
	{
		

		isPalindrome(i);
	
			System.out.println(i);
	}
		
	}

}
