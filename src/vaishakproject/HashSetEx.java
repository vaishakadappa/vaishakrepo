package vaishakproject;
import java.util.HashSet;
import java.util.Iterator;
public class HashSetEx {
public static void main(String[] args) {
	HashSet<Character> h=new HashSet<Character>();
	h.add('a');
	h.add('e');
	h.add('V');
	h.add('v');
	System.out.println("using for each loop");
	for(Character i:h)
	{
		System.out.println(i);
		
	}
	System.out.println("using iterator");
	Iterator<Character>ab=h.iterator();
	while(ab.hasNext())
	{
		System.out.println(ab.next());
	}

}
}
