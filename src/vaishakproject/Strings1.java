package vaishakproject;

public class Strings1 {

	public static void main(String[] args) {
		//approach 1
		String s="vaishak adappa";
		
		char[] charr = s.trim().toCharArray();
		
		for(int i=charr.length-1;i>=0;i--) {
			System.out.print(charr[i]);
		}
		System.out.println("");
		//approach 2
		for(int i=s.length()-1;i>=0;i--) {
			System.out.print(s.charAt(i));
		}
		System.out.println("");
		//approach 3
		StringBuffer buff=new StringBuffer(s);
		System.out.print(buff.reverse());
		
		//count the occurance of a
		int total=s.length();
		int afterremoving = s.replace("a","").length();
		int count = total-afterremoving;
		System.out.println(count);
		
		//swaping two numbers
		int a=20,b=40;
		
		System.out.println("before swapping"+ a+" "+ b);
		
		int c=a;
		a=b;
	    b=c;
	    System.out.println("after swapping"+ a+" "+ b);
	}

}
