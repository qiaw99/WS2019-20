package Test;

import java.util.ArrayList;

/**
 *   mensch  wolf  ziege  kohlkopf
 * 	  0     0      0        0
 * @author 87290
 *
 */

class State{
	public int mensch;
	public int wolf;
	public int ziege;
	public int kohlkopf;
}

class Vertex{
	State objstate = new State();
	String outputMessage;
	
	public Vertex(int mensch, int wolf, int ziege, int kohlkopf, String outputMessage) {
		objstate.mensch = mensch;
		objstate.wolf = wolf;
		objstate.kohlkopf = kohlkopf;
		this.outputMessage = outputMessage;
	}
}

class Test{
	public static void matrixInitialize(int arr[][]) {
		for(int i = 0; i < arr.length; i++) {
			for(int j = 0; j < arr[i].length; j++) {
				arr[i][j] = 0;
			}
		}
	}
	
	/**
	 * Es kann nur unten 10 möglichen Situationen geben, ansonsten kommt es zum Konflikt
	 * @param arrayList
	 */
	public static void addSituations(ArrayList<Vertex> arrayList) {
		arrayList.add(new Vertex(0, 0, 0, 0, "Initializierung"));
		arrayList.add(new Vertex(0, 1, 0, 0, "mensch ziege kohlkopf | wolf"));
		arrayList.add(new Vertex(0, 0, 1, 0, "mensch wolf kohlkopf | ziege"));
		arrayList.add(new Vertex(0, 0, 0, 1, "mensch wolf ziege | kohlkopf"));
		arrayList.add(new Vertex(1, 0, 1, 0, "wolf kohlkopf | mensch ziege"));
		arrayList.add(new Vertex(0, 1, 0, 1, "mensch ziege | wolf kohlkopf"));
		arrayList.add(new Vertex(1, 0, 1, 1, "wolf | mensch ziege kohlkopf"));
		arrayList.add(new Vertex(1, 1, 0, 1, "ziege | mensch wolf kohlkopf"));
		arrayList.add(new Vertex(1, 1, 1, 0, "kohlkopf | mensch wolf ziege"));
		arrayList.add(new Vertex(1, 1, 1, 1, "Fertig"));
	}
}

public class U7_53 {
	public static int[][] arr = new int[10][10];
	public static ArrayList<Vertex> arrayList = new ArrayList<Vertex>();
	public static int[] visited = new int[10];
	
	public static void main(String args[]) {
		Test.matrixInitialize(arr);
		Test.addSituations(arrayList);
		System.out.println();
	}
}
