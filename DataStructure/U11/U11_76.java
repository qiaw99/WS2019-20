package Test;

@SuppressWarnings("serial")
class ResultFounded extends Exception{}

class Drachen{
	int n;	//n Drachen auf einem nxn Schachbrett
	int [][] res;
	long counter;
	
	public Drachen(int n) {
		this.n = n;
		this.counter = 0;
		res = new int[n][n];
		try {
			put(0);
		}catch(ResultFounded e){
			
		}
	}
	
	public void put(int x) throws ResultFounded{
		if(x == n) {
			throw new ResultFounded();
		}else {
			for(int i = 1; i <= n; i++) {
				for (int j = 1; j <= n; j++) {
					if(!conflict(i, j, x)) {
						res[i][j] = 1;
						counter ++;
						put(x + 1);
					}
				}
			}
		}
	}

	public boolean conflict(int i, int j, int k) {
		int sum = 0;
		int temp = 0;
		for(int a = 0; a < n; a++) {
			// check the raw
			for(int b = 0; b < n; b++) {
				sum += res[a][b];
				// check the column
				temp += res[b][a];
			}
			if(sum > 1 || temp > 1) {
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
