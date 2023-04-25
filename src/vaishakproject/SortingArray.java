package vaishakproject;

public class SortingArray {

	public static void main(String[] args) {
int a[]= {2,4,5,6,7,3};
int temp;
	for (int i = 0; i < a.length; i++) {
		for (int j = i+1; j < a.length; j++) {
			if(a[i]>a[j]) {
				//temp=a[i]; 
				a[i]=a[i]+a[j];
				a[j]=a[i]-a[j];
				a[i]=a[i]-a[j];
				//a[i]=a[j];
				//a[j]=temp;
				
			}
			
		}
		System.out.print(a[i]+ " ");
	}
	
	}}

