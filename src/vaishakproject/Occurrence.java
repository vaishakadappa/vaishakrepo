package vaishakproject;

public class Occurrence {

	public static void main(String[] args) {

		String str = "vaishak adappa";
		int[] count = new int[256];

		for (int i = 0; i < str.length(); i++) {
			count[str.charAt(i)]++;
		}

		for (int i = 0; i < 256; i++) {
			if (count[i] > 0 && Character.isLetter((char) i)) {
				System.out.println((char) i + " " + count[i]);
			}
		}
		
	}
}
