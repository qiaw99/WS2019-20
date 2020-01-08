/**
 * @author Qianli Wang and Nazar Sopiha
 */

@SuppressWarnings("serial")
class ResultFound extends Exception{
    private String msg;
    
    public ResultFound(String msg){
        super(msg);        
        this.msg = msg;
    }
}

class Drachen{
	private int n;	//n Drachen auf einem nxn Schachbrett
	private int [][] res;
	private boolean [][] capture;
	private long counter;
	
	public Drachen(int n) {
		this.n = n;
		this.counter = 0;
		res = new int[n][n];
		capture = new boolean[n][n];
		initialize();
		
		try {
			put(0);
		}catch(ResultFound e){
			e.printStackTrace();
		}finally{
			System.out.println("Counter = " + this.counter);
		}
	}
	
	private void initialize() {
		for(int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				res[i][j] = 0;
				capture[i][j] = false;
			}
		}
	}
	
	private void add(int i, int j) {
		for(int a = 0; a < n; a++) {
			// Spalte checken
			capture[a][j] = true;
			// Zeile checken
			capture[i][a] = true;
		}
		// 4 Quad, Diag
		int a = i,b = j;																																																																																																																																																																																				
		while(a < n - 1 && b < n - 1) {
			capture[++a][++b] = true;
		}
		
		// 1 Quad Diag
		a = i;
		b = j;																																																																																																																																																																																				
		while(a < n - 1 && b > 0) {
			capture[++a][--b] = true;
		}
		
		// 2 Quad Diag
		a = i;
		b = j;																																																																																																																																																																																				
		while(a > 0 && b > 0) {
			capture[--a][--b] = true;
		}
		
		// 3 Quad Diag
		a = i;
		b = j;																																																																																																																																																																																				
		while(a > 0 && b < n - 1) {
			capture[--a][++b] = true;
		}
		
		//Springer
		a = i;
		b = j;
		if (a - 2 >= 0) {
			if (b - 1 >= 0) {
				capture[a - 2][b - 1] = true;
			}
			if (b + 1 < n) {
				capture[a - 2][b + 1] = true;
			}
		}
		
		if (a + 2 < n) {
			if (b - 1 >= 0) {
				capture[a + 2][b - 1] = true;
			}
			if (b + 1 < n) {
				capture[a + 2][b + 1] = true;
			}
		}
		
		if (b - 2 >= 0) {
			if (a - 1 >= 0) {
				capture[a - 1][b - 2] = true;
			}
			if (a + 1 < n) {
				capture[a + 1][b - 2] = true;
			}
		}
		
		if (b + 2 < n) {
			if (a - 1 >= 0) {
				capture[a - 1][b + 2] = true;
			}
			if (a + 1 < n) {
				capture[a + 1][b + 2] = true;
			}
		}
		
	}
	
	private void put(int x) throws ResultFound{
		// TODO
		if(isFull()) {
			throw new ResultFound("Result is found!");
		}else {
			for(int i = 0; i < n; i++) {
				for (int j = 0; j < n; j++) {
					if (!conflict(i,j)) {
						add(i,j);
						counter++;
						res[i][j] = 1;
						put(x + 1);
					}
				}
			}
		}
	}

	private boolean isFull () {
		for(int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (capture[i][j] == false)
					return false;
			}
		}
		return true;
	}

	private boolean conflict (int i, int j) {
		if (capture[i][j] == true) 
			return true;
		return false;
	}
	
    public long getCounter(){
        return this.counter;
    }
    
	public void print() {
		for(int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				System.out.print(res[i][j] + " ");
			}
			System.out.println();
		}
	}
}

public class U11_76 {
    public static int findMin(){
        for (int i = 2; i < 100; i++) {
            if (new Drachen(i).getCounter() == i) {
                return i;
            }
        }
        // -1 means ERROR
        return -1;
    }
    
	public static void main(String[] args) throws Exception{
		if(args.length == 0) {
			new Drachen(8).print();
		}else if(args.length == 1){
			new Drachen(Integer.parseInt(args[0])).print();
		}else{
            throw new Exception("Too much parameters!");
        }
        System.out.println("Auf dem 11x11 Schachbrett können 11 Drachen aufstellen");
	}
}
