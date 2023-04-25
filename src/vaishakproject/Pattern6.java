package vaishakproject;

public class Pattern6 {

	public static void main(String[] args) {
		int[] x= {23,45,65,78,67,67};
		int small=getSmallest(x);
				System.out.println("smallest is:"+ small);
	
		// TODO Auto-generated method stub

	}
	public static int getSmallest(int[] n)
	{
		int small=n[0];
		for(int i=1;i<n.length;i++)
		{
			if(n[i]<small)
				small=n[i];
			
		}
		return small;
	}

}
