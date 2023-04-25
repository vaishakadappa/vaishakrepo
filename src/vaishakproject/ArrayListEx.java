package vaishakproject;

import java.util.ArrayList;

public class ArrayListEx {
    String name;
    int id;

    public ArrayListEx(String name, int id) {
        this.name = name;
        this.id = id;
    }

    public String toString() {
        return name + " " + id;
    }

    public static void main(String[] args) {
        ArrayList<ArrayListEx> al = new ArrayList<ArrayListEx>();
        al.add(new ArrayListEx("vaishak", 123));
        al.add(new ArrayListEx("va", 123));
        for (ArrayListEx i : al) {
            System.out.println(i);
        }
    }
}