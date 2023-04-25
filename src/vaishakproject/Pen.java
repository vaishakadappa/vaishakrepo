package vaishakproject;

import java.util.ArrayList;
import java.util.ListIterator;

public class Pen {
	String brand;
	int price;
	
	Pen(String brand, int price) {
	
		this.brand = brand;
		this.price = price;
	}
public String toString()
{
	return brand+" "+price;
}

	public static void main(String[] args) {
ArrayList<Pen> al=new ArrayList<Pen>();
al.add(new Pen("camel",49));
al.add(new Pen("rolex",49));
al.add(new Pen("martin",49));
al.add(new Pen("apsara",49));
ListIterator i=al.listIterator();
System.out.println("forward direction");
while(i.hasNext())
{
	System.out.println(i.next());
}
System.out.println("backward direction");
while(i.hasPrevious())
{
	System.out.println(i.previous());
}
	}	}