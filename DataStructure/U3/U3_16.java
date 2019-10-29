class TreeNode{
	public int key;
	public TreeNode left, right, parent;
	
	public TreeNode(int key){
		this.key = key;
	}
}

class BinarySearchTree{
	public TreeNode root;
	
	public BinarySearchTree(){
		root = null;
	}
	
	public void inOrder(TreeNode x) {
		if(x != null) {
			inOrder(x.left);
			System.out.print(x.key + " ");
			inOrder(x.right);
		}
	}

	public void insert(BinarySearchTree T, TreeNode z) {
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

public class U3_16{
	public static void main(String args[]){
		int[] arr = new int []{5,4,3,2,1};
		BinarySearchTree tree = transform(arr);
		tree.inOrder(tree.root);
		System.out.println();
	}

	public static BinarySearchTree transform(int [] arr){
		BinarySearchTree tree = new BinarySearchTree();
		for(int i = 0; i < arr.length; i++){
			tree.insert(tree, new TreeNode(arr[i]));
		}
		return tree;
	}
}
