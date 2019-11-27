import java.util.ArrayList;

/**
 *   mensch  wolf  ziege  kohlkopf
 * 	  0     0      0        0
 * @author Qianli Wang und Nazar Sopiha
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
    /*
    public static void matrixInitialize(int arr[][]) {
        for(int i = 0; i < arr.length; i++) {
            for(int j = 0; j < arr[i].length; j++) {
                arr[i][j] = 0;
            }
        }
    }
    */

    /**
     * Das Status vom Menschen muss geändert werden, und das Status einer von den anderen
     * Teilnehmern muss geändert werden.
     * @param arr
     */
    public static void matrixAdd(int arr[][], ArrayList<Vertex> arrayList){
        for(int i = 0; i < arr.length; i++){
            // Status davor
            int mensch_i = arrayList.get(i).objstate.mensch;
            int wolf_i = arrayList.get(i).objstate.wolf;
            int ziege_i = arrayList.get(i).objstate.ziege;
            int kohlkopf_i = arrayList.get(i).objstate.kohlkopf;
            for(int j = 0; j < arr[i].length; j++){
                //Status danach
                int mensch_j = arrayList.get(j).objstate.mensch;
                int wolf_j =arrayList.get(j).objstate.wolf;
                int ziege_j =arrayList.get(j).objstate.ziege;
                int kohlkopf_j =arrayList.get(j).objstate.kohlkopf;
                if(mensch_i != mensch_j && (Math.abs(wolf_i - wolf_j) + Math.abs(ziege_i - ziege_j) + Math.abs(kohlkopf_i - kohlkopf_j) == 1)){
                    arr[i][j] = 1;
                }else
                    arr[i][j] = 0;
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
    //public static int[] visited = new int[10];

    public static void main(String args[]) {
        Test.addSituations(arrayList);
        Test.matrixAdd(arr, arrayList);
        Test.printMatrix(arr);
        System.out.println();
    }
}
