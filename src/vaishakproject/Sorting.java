package vaishakproject;

import java.util.ArrayList;
import java.util.Collections;
public class Sorting {
	public static void main(String[] args) {
		ArrayList<Float> al=new ArrayList<Float>();
		al.add(23.3f);
		al.add(2.3f);
		al.add(3.4f);
		al.add(23.4f);
		System.out.println("beforing sorting");
		for(Float i: al)
		{
		System.out.println(i);
		}
		System.out.println("after sorting");
		Collections.sort(al);
		for(Float i: al)
		{
		System.out.println(i);
		}
		
}}
