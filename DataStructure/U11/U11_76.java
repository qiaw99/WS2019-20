@SuppressWarnings("serial")
class ResultFound extends Exception{}

class Drachen{
	int n;	//n Drachen auf einem nxn Schachbrett
	int [][] res;
	boolean [][] capture;
	long counter;
	
	public Drachen(int n) {
		this.n = n;
		this.counter = 0;
		res = new int[n][n];
		capture = new boolean[n][n];
		initialize();
		
		try {
			put(0);
		}catch(ResultFound e){
			//System.out.println("Error trace: " + e.printStackTrace());
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
	
	public void add(int i, int j) {
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
	
	public void put(int x) throws ResultFound{
		// TODO
		if(isFull()) {
			throw new ResultFound();
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

	public boolean isFull () {
		for(int i = 0; i < n; i++) {
			for (int j = 0; j < n; j++) {
				if (capture[i][j] == false)
					return false;
			}
		}
		return true;
	}

	public boolean conflict (int i, int j) {
		if (capture[i][j] == true) 
			return true;
		return false;
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
	public static void main(String[] args) {
		if(args.length == 0) {
			for (int i = 2; i < 100; i++) {
				if (new Drachen(i).counter == i) {
					System.out.println(i);
				}
				
			}
			
		}else {
			new Drachen(Integer.parseInt(args[0]));
		}
	}
}
