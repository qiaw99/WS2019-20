public class U3_22{
	public static void main(String args[]){
		Node n1 = new Node(1,1);
		Node n2 = new Node(3,4);
		Node n3 = new Node(5.5,3);
		Node n4 = new Node(7,1.5);
		Node[] arr = new Node[]{n1,n2,n3,n4};
		System.out.println(new ConstantFunction(arr).calculate(2.0));
	}
}

class Node{
	public double first;
	public double second;

	public Node(double first, double second){
		this.first = first;
		this.second = second;
	}
}

class ConstantFunction{
	private Node[] arr;

	/**
	 * Assume that the object list is sorted according to the first element.
	 * @param arr
     */
	public ConstantFunction(Node[] arr){
		this.arr = arr;
	}

	public double calculate(double x){
		int i = 0;
		while(arr[i].first < x){
			i++;
		}
		int temp = i - 1;
		double coefficient = (arr[temp].second-arr[i].second) / (arr[temp].first-arr[i].first);
		return (arr[temp].second - coefficient * arr[temp].first + coefficient * x);
	}
}
