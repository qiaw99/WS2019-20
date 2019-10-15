package U1;

import java.util.Random;

public class Quicksort {
	public static void main(String args[]) {
		float arr[] = new float[] {2,3,1,4,5};
		qSort(arr, 0, 4);
		for(float i : arr) {
			System.out.print(i + " ");
		}
	}
	
	public static float[] qSort(float[] arr, int low ,int high) {
		if(low < high) {
			int q = random_partition(arr, low ,high);
			qSort(arr, low, q - 1);
			qSort(arr, q + 1, high);
		}
		return arr;
	}
	
	public static void exchange(float[] arr, int i, int j) {
		// Exchange arr[i] with arr[j]
		float temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	public static int partition(float[] A, int p, int r) {
		float x = A[r];
		int i = p - 1; 
		for(int j = p; j < r; j++) {
			if(A[j] <= x) {
				i += 1;
				exchange(A, i, j);
			}
		}
		exchange(A, i + 1, r);
		return i+1;
	}
	
	public static int random_partition(float[]A , int p, int r) {
		Random random = new Random();
		//[0,r-p+1) -> [p,r+1) -> [p,r]
		int i = random.nextInt(r - p + 2) + p;
		exchange(A, r, i);
		return partition(A, p, r);
	} 
}
