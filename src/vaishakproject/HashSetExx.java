package vaishakproject;
import java.util.HashSet;
public class HashSetExx {
public static void main(String[] args) {
	HashSet<Object> h=new HashSet<Object>();
	h.add("btm");
	h.add("qspider");
	h.add("jpnagar");
	for(Object i:h)
	{
		System.out.println(i);
	}
	h.remove("btm");
	System.out.println("AFTER REMOVING");

	for(Object i:h)
	{
		System.out.println(i);
	}
	
}
}

