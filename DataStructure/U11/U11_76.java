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
		// 1 Diag
		int a = i,b = j;																																																																																																																																																																																				
		while(a < n && b < n) {
			capture[++a][++b] = true;
		}
		
		// 2 Diag
		a = i;
		b = j;																																																																																																																																																																																				
		while(a < n && b < n) {
			capture[++a][++b] = true;
		}
		
		a = i;b = j;																																																																																																																																																																																				
		while(a < n && b < n) {
			capture[++a][++b] = true;
		}
		
		a = i;b = j;																																																																																																																																																																																				
		while(a < n && b < n) {
			capture[++a][++b] = true;
		}
		
	}
	
	public void put(int x) throws ResultFound{
		// TODO
		if(x == n) {
			throw new ResultFound();
		}else {
			for(int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					if(!conflict(i, j, x)) {
						res[i][j] = 1;
						capture[i][j] = true;
						add(i, j);
						counter ++;
						put(x + 1);
					}
				}
			}
		}
	}

	public boolean conflict(int i, int j, int k) {
		int sum = 0;
		int capture = 0;
		for(int a = 0; a < n; a++) {
			// check the raw
			for(int b = 0; b < n; b++) {
				sum += res[a][b];
				// check the column
				capture += res[b][a];
			}
			if(sum > 1 || capture > 1) {
				return true;
			}else {
				sum = 0;
			}
		}
		return false;
	}
	
	public void print() {
		for(int i = 1; i <= n; i++) {
			for (int j = 1; j <= n; j++) {
				
			}
		}
	}
}

public class U11_76 {
	public static void main(String[] args) {
		if(args.length == 0) {
			new Drachen(8);
		}else {
			new Drachen(Integer.parseInt(args[0]));
		}
	}
}
