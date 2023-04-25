package vaishakproject;

public class Space {

	public static void main(String[] args) {
		int n=5;
		// TODO Auto-generated method stub
for(int i=1;i<=n;i++)
{
	for(int j=1;j<=i-1;j++)
	{
		System.out.print(" ");
	}
	for(int j=n;j>=i;j--)
	{
		System.out.print(j);
	}
	System.out.println("");
}
	}

}
