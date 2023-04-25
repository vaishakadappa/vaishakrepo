package vaishakproject;

	import java.util.Scanner;

	public class StringOccurrence {
	    public static void main(String[] args) {
	        Scanner scanner = new Scanner(System.in);

	        System.out.println("Enter the input string: ");
	        String input = scanner.nextLine();

	        String stringToCount = "a";

	        int count = countOccurrences(input, stringToCount);

	        System.out.println("The string \"" + stringToCount + "\" occurs " + count + " times in the input string.");
	    }

	    public static int countOccurrences(String input, String stringToCount) {
	        int count = 0;
	        int index = 0;

	        while ((index = input.indexOf(stringToCount, index)) != -1) {
	            count++;
	            index += stringToCount.length();
	        }

	        return count;
	    }
	}
	

	
