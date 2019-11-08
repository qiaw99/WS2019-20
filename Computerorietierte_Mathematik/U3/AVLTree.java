package Test;

class BinarySearchTree{
	private class TreeNode{
		public int key;
		public TreeNode left, right, parent;
		public int height;
		
		public TreeNode(int key){
			this.key = key;
			height = 0;
		}
	}
	
	public TreeNode root;
	
	public BinarySearchTree(){
		root = null;
	}
	
	private int getHeight(TreeNode n) {
		if(n == null) {
			return 0;
		}
		return n.height;
	}
	
	// The difference of the heights
	private int balance(TreeNode n) {
		if(n == null) {
			return 0;
		}
		return getHeight(n.left) - getHeight(n.right);
	}
	
	private void inOrder(TreeNode x) {
		if(x != null) {
			inOrder(x.left);
			System.out.print(x.key + " ");
			inOrder(x.right);
		}
	}

	private TreeNode treeSearch(TreeNode x, int k) {
		if(x == null || k == x.key) {
			return x;
		}
		if(k < x.key) {
			return treeSearch(x.left, k);
		}else {
			return treeSearch(x.right, k);
		}
	}
	
	private TreeNode maximum(TreeNode x) {
		while(x.right != null) {
			x = x.right;
		}
		return x;
	}
	
	private TreeNode minimum(TreeNode x) {
		while(x.left != null) {
			x = x.left;
		}
		return x;
	}
	
	private TreeNode successor(TreeNode x) {
		if(x.right != null) {
			return minimum(x.right);
		}
		TreeNode y = x.parent;
		while(y != null && x == y.right) {
			x = y;
			y = y.parent;
		}
		return y;
	}
	
	private TreeNode insert(TreeNode n, int key) {
		if(n == null) {
			return (new TreeNode(key));
		}
		
		// Find the right position and insert the node 
		if(key < n.key) {
			n.left = insert(n.left, key);
		}else {
			n.right = insert(n.right ,key);
		}
		
		n.height = Math.max(n.left.height, n.right.height) + 1;
		return n;
	}
	
	private TreeNode leftRotate(TreeNode x) {
		TreeNode y = x.right;
		TreeNode p = x.parent;
		
		// Parent with y
		if(p.right.equals(x)) {
			p.right = y;
		}else {
			p.left = y;
		}
		y.parent = p;
		
		// The relation between x and y
		y.left = x;
		x.parent = y;
		
		// The left tree of y
		x.right = y.left;
		y.left.parent = x;
		
		// Update the height
		x.height = Math.max(getHeight(x.left), getHeight(x.right)) + 1;
		y.height = Math.max(getHeight(y.left), getHeight(y.right)) + 1;
		
		return y;
	}
	private void delete(BinarySearchTree T, TreeNode z) {

	}
}

public class AVLTree {

}
