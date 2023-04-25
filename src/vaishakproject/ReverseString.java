package vaishakproject;

import java.util.Iterator;

public class ReverseString {

	public static void main(String[] args) {
		String s = "welcome to the world";
		String[] str = s.split(" ");

		String reversedword = "";

		for (String word : str) {

			String reverse = "";
			for (int i = word.length() - 1; i >= 0; i--) {
              
				reverse = reverse + word.charAt(i);
			}
			reversedword = reversedword + reverse + " ";
		}
		
		System.out.println(reversedword);

	}

}
