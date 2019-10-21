package U1;

import java.util.Random;

/**
 * As an alternative of quicksort, we use bubblesort.
 * @author Qianli and Nazar
 */

public class Quicksort {
	// "counter" is used to count the number of comparisons
	public static long counter = 0;
	public static final int SIZE = 20000000;
	public static Random random = new Random();
	public static long b = 10000;
	/*
	 * Assume that b = 100000
	 * The best length with bubblesort is 7600. 
	 */
	
	public static void main(String args[]) {
		float arr[] = new float[SIZE]; 
		float temp;
		
		System.out.println("The bubblesort is called with max length: " + b);
		
		for(int i = 0; i < SIZE; i ++) {
			/* Produce float within the interval [0,2).
			 * With the help of nextFloat(), the probability
			 * of one float whose value is between [0,1]
			 * is equally distributed.
			 */
			temp = 2 * random.nextFloat();
			while(temp > 1) {
				temp = 2 * random.nextFloat();
			}
			arr[i] = temp;
		}
		
		// Get the start time with unit "ms"
		long startTime = System.currentTimeMillis();   
		
		qSort(arr, 0, SIZE - 1);
		
		long endTime = System.currentTimeMillis(); 
		System.out.println("The running time of this programm is: " + (endTime - startTime) + "ms");  
		
		/*
		for(float i : arr) {
			System.out.print(i + " ");
		}
		System.out.println();
		*/
		
		System.out.println("The number of comparisons: " + counter);
	}
	
	public static float[] qSort(float[] arr, int low ,int high) {
		if(low < high) {
			int q = random_partition(arr, low ,high);
			
			if(q - 1 - low > b) {
				qSort(arr, low, q - 1);
			}else {
				bubblesort(arr, low, q - 1);
			}
			
			if(high - q - 1 > b) {
				qSort(arr, q + 1, high);
			}else {
				bubblesort(arr, q + 1, high);
			}
		}
		return arr;
	}
	/**
	 * Exchange arr[i] with arr[j]
	 * @param arr
	 * @param i
	 * @param j
	 */
	public static void exchange(float[] arr, int i, int j) {
		float temp = arr[i];
		arr[i] = arr[j];
		arr[j] = temp;
	}

	public static int partition(float[] arr, int p, int r) {
		float x = arr[r];
		int i = p - 1; 
		for(int j = p; j < r; j++) {
			if(arr[j] <= x) {
				i += 1;
				counter ++;
				exchange(arr, i, j);
			}
		}
		exchange(arr, i + 1, r);
		return i + 1;
	}
	
	public static int random_partition(float[] arr , int p, int r) {
		//[0,r-p+1) -> [p,r+1) -> [p,r]
		int i = random.nextInt(r - p + 1) + p;
		exchange(arr, r, i);
		return partition(arr, p, r);
	} 
	
	//Bubblesort(within exact interval) implements
	public static float[] bubblesort(float[] arr, int i, int j) {
		boolean swap = true;
		int stop = j - i;
		while(swap) {
			swap = false;
			for(int temp = i; temp < stop; temp ++) {
				if(arr[temp] > arr[temp + 1]) {
					counter ++; 
					exchange(arr, temp, temp + 1);
					swap = true;
				}
			}
			stop = stop - 1;
		}
		return arr;
	}
}

