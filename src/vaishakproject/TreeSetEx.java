package vaishakproject;

	import java.util.TreeSet;

	public class TreeSetEx {
	    public static void main(String[] args) {
	       TreeSet<String> treeSet = new TreeSet<>();
	        treeSet.add("bttm");
            treeSet.add("btnn");
            
           
	        try {
	        	
	            treeSet.add(null);  // adding null value to the TreeSet]
	           
	        } 
	        catch (NullPointerException e) 
	        {
	            System.out.println("Error: " + e);
	        }
	            finally 
	   	        {
	   	            System.out.println("All ok");
	   	        }
	        
            System.out.println("using for each loop");
            for(String i:treeSet) {
            	System.out.println(i);
            }
    }
}
	  
				  
	


