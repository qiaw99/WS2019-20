import java.util.ArrayList;

/**
 * 	 Sequenz:
 *   mensch  wolf  ziege  kohlkopf
 * 	  0       0      0       0
 * @author Qianli Wang und Nazar Sopiha
 */

class Vertex{
    State objstate = new State();
    String outputMessage;

    public Vertex(int mensch, int wolf, int ziege, int kohlkopf, String outputMessage) {
        objstate.mensch = mensch;
        objstate.wolf = wolf;
        objstate.kohlkopf = kohlkopf;
        objstate.ziege = ziege;
        this.outputMessage = outputMessage;
    }
    
    public class State{
        public int mensch;
        public int wolf;
        public int ziege;
        public int kohlkopf;
    }
}

class Test{
    /**
     * Das Status vom Menschen muss geändert werden, und das Status maximal einer von den anderen
     * Teilnehmern kann geändert werden. Das Matrix wird mit 0 oder 1 durch Überprüfungen von den
     * Bedingungen initialisiert.
     * @param arr
     */
    public static void matrixInitialize(int arr[][], ArrayList<Vertex> arrayList){
    	int num = 0;
        for(int i = 0; i < arr.length; i++){
            // Status before
        	// arrayList.get(i) -> Objekte von Vertex
            int mensch_i = arrayList.get(i).objstate.mensch;
            int wolf_i = arrayList.get(i).objstate.wolf;
            int ziege_i = arrayList.get(i).objstate.ziege;
            int kohlkopf_i = arrayList.get(i).objstate.kohlkopf;
            
            for(int j = 0; j < arr[i].length; j++){
                //Status after
                int mensch_j = arrayList.get(j).objstate.mensch;
                int wolf_j = arrayList.get(j).objstate.wolf;
                int ziege_j = arrayList.get(j).objstate.ziege;
                int kohlkopf_j = arrayList.get(j).objstate.kohlkopf;
                
                if(mensch_i != mensch_j && (Math.abs(wolf_i - wolf_j) + Math.abs(ziege_i - ziege_j) + Math.abs(kohlkopf_i - kohlkopf_j) <= 1)){
                    arr[i][j] = 1;
                    num ++;
                }else {
                    arr[i][j] = 0;
                }
            }
        }
    }

    public static void printMatrix(int arr[][]){
        for(int i = 0; i < arr.length; i++){
            for(int j = 0; j < arr[i].length; j++){
                System.out.print(arr[i][j]);
            }
            System.out.println();
        }
    }

    /**
     * Es kann nur unten 10 möglichen Situationen geben, ansonsten kommt es zum Konflikt
     * @param arrayList
     */
    public static void addSituations(ArrayList<Vertex> arrayList) {
        arrayList.add(new Vertex(0, 0, 0, 0, "Initialisierung"));
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
    
    /**
     * Die ganze Graph wird durchgegangen
     * @param start
     * @param end
     * @param arr
     * @param hasVisited
     * @param arrayList
     */
    public static void traversal(int start, int end, int arr[][], int[] hasVisited, ArrayList<Vertex> arrayList) {
    	if(start == end) {
    		showResult(end, hasVisited, arrayList);
    		System.out.println();
    	}else {    	
	    	for(int i = 0; i < arr.length; i++) {
	    		// Wenn es noch eine Kante gibt und noch nicht besucht wird
	    		if(arr[start - 1][i] == 1 && hasVisited[i] == 0) {
	    			hasVisited[i] = start;
	    			traversal(i + 1, end, arr, hasVisited, arrayList);
	    			hasVisited[i] = 0;
	    		}
	    	}
    	}
    }
    
    public static void showResult(int end, int[] hasVisited, ArrayList<Vertex> arrayList) {
    	// Die Liste wird von hinten nach vorne durchgegangen und von vorne nach hinten ausgedruckt.
    	// In temp wird die umgekehrte Sequenz gespeichert
        int[] temp = new int[10]; 
        // Die Anzahl der Elemente
        int num = 0;    
        int index = end;   
        
        while (index != 1) {
            // Suchen nach vorne, bis das erste Element
            temp[num] = hasVisited[index - 1];
            index = temp[num];
            num ++;     
        }
        for (int j = num - 1; j >= 0; j--) {
            System.out.println(6-j + ": " + arrayList.get(temp[j] - 1).outputMessage);
        }
        // Das Endstatus -> Fertig
        System.out.println(arrayList.get(9).outputMessage);
    }
}

public class U7_53 {
    public static int[][] arr = new int[10][10];
    public static ArrayList<Vertex> arrayList = new ArrayList<Vertex>();
    // hasVisited ist eine Liste, die den Knoten, der den jetzigen Knoten besucht, speichert.
    public static int[] hasVisited = new int[10];

    public static void main(String args[]) {
        // Explizit definiert
    	hasVisited[0] = 1;
        Test.addSituations(arrayList);
        Test.matrixInitialize(arr, arrayList);
        
        System.out.println("Adjazenzmatrix: ");
        Test.printMatrix(arr);
        System.out.println();
        
        Test.traversal(1, 10, arr, hasVisited, arrayList);
        System.out.println("Es gibt insgesamt 20 Kanten und 10 Knoten.");
    }
}
