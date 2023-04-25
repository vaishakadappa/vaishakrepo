package vaishakproject;

import java.util.ArrayList;
import java.util.Collections;

public class IntegerArr {
	public static void main(String[] args) {
		ArrayList<Integer> al=new ArrayList<Integer>();
		al.add(23);
		al.add(87);
		al.add(33);
		al.add(233);
		System.out.println("beforing sorting");
		for(Integer i: al)
		{
		System.out.println(i);
		}
		System.out.println("after sorting");
		Collections.sort(al);
		for(Integer i: al)
		{
		System.out.println(i);
		}
}}
