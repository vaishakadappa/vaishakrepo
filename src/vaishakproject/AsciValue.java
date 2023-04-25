package vaishakproject;

public class AsciValue {

	public static void main(String[] args) {
		/*
		 * for (int i = 0; i <= 128; i++) { char c=(char)i;
		 * System.out.println(c+"-->"+i);
		 * 
		 * }
		 */
		String str = "vaishak adappa"; // v-1 a-5
		countLetters(str);

	}

	private static void countLetters(String str) {
		char[] ch = str.toCharArray();

		boolean ck[] = new boolean[ch.length];

		for (int i = 0; i < ch.length; i++) {
			if (ck[i] == false) {
				int count = 1;

				for (int j = i + 1; j < ch.length; j++) {
					if (ch[i] == ch[j]) {
						count++;
						ck[j] = true;
					}
				}
				System.out.println(ch[i] + "=" + count);
			}

		}

	}
}
