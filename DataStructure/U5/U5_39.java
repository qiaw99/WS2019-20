class TreeNode{
	public int key;
	public TreeNode left, right, parent;
	
	public TreeNode(int key){
		this.key = key;
	}
}

class BinarySearchTree{
	public TreeNode root;
	public int nodes;
	
	public BinarySearchTree(){
		root = null;
		nodes = 0;
	}

	public int getTotal(){
		int total = 0;
		return (getInternalLength(root.left) + getInternalLength(root) + getInternalLength(root.right)) / this.getSize();
	}

	public int getSize(){
		return this.nodes;
	}

	public int getInternalLength(TreeNode n){
		int counter = 0;
		if(n == root)
			return counter;
		while(n != root){
			counter ++;
			n = n.parent;
		}
		return counter;
	}
	
	public void inOrder(TreeNode x) {
		if(x != null) {
			inOrder(x.left);
			System.out.print(x.key + " ");
			inOrder(x.right);
		}
	}

	public void insert(BinarySearchTree T, TreeNode z) {
		nodes ++;
		TreeNode y = null;
		TreeNode x = T.root;
		while(x != null) {
			y = x;
			if(z.key < x.key) {
				x = x.left;
			}else {
				x = x.right;
			}
		}
		z.parent = y;
		if(y == null) {
			T.root = z;
		}else if(z.key < y.key) {
			y.left = z;
		}else {
			y.right = z;
		}
	}
}

public class U5_39{
	public static void main(String args[]){
		int[] arr = new int []{5,4,3,2,1};
		BinarySearchTree tree = transform(arr);
		tree.inOrder(tree.root);
		System.out.println(tree.getTotal());
	}

	public static BinarySearchTree transform(int [] arr){
		BinarySearchTree tree = new BinarySearchTree();
		for(int i = 0; i < arr.length; i++){
			tree.insert(tree, new TreeNode(arr[i]));
		}
		return tree;
	}
}
