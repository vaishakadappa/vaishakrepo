package vaishakproject;
import java.util.LinkedList
;
import java.util.ListIterator;
public class Bidirectional {
public static void main(String[] args) {
	LinkedList al=new LinkedList();
	al.add("btm");
	al.add(23);
	al.add(23f);
	al.add(233);
	ListIterator i=al.listIterator();
	System.out.println("forward");
	while(i.hasNext())
	{
		System.out.println(i.next());
	}
	System.out.println("backward direction");
	while(i.hasPrevious())
	{
		System.out.println(i.previous());
	}
}
}
