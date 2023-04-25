package vaishakproject;

import java.util.ArrayList;

public class ArrayListEx1 {
	public static void main(String[] args) {
		ArrayList<Float> al=new ArrayList<Float>();
		al.add(23.3f);
		al.add(2.3f);
		al.add(3.4f);
		al.add(23.4f);
		for(int i=0;i<al.size();i++)
		{
			System.out.println(al.get(i));
		}
		for(Float i:al)
		{
			System.out.println(i);
		}
		System.out.println(al.contains(2.5f));
		al.add(3,10.2f);
		
		for(Float i: al)
		{
		System.out.println(i);
		}
	}
	

}
