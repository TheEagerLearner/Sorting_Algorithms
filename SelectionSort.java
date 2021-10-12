package testCode;

public class SelectionSort {
	
	static void sort(int[] arr, int n) {
		
		for(int i=0; i<n-1; i++) {
			int min = arr[i];
			
			for(int j = i+1; j<n; j++) {
				if(arr[j] < min) {
					min = arr[j];
					int temp = arr[j];
					arr[j] = arr[i];
					arr[i] = temp;
				}
			}
		}
		
	}
	
	static void printArr(int[] arr, int n) {
		
		for(int i=0; i<n; i++) {
			System.out.print(arr[i] + " ");
		}
		
	}

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		int arr[] = {64,25,12,22,11};
		int len = arr.length;
		sort(arr, len);
		System.out.println("Sorted Array:");
		printArr(arr, len);

	}

}
