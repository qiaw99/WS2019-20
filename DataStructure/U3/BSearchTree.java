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
	
	/**
	 * Invoke this function with parameter "root" to get all element in the tree.
	 * Running time : Θ(n)
	 * @param x
	 */
	public void inOrder(TreeNode x) {
		if(x != null) {
			inOrder(x.left);
			System.out.print(x.key + " ");
			inOrder(x.right);
		}
	}
	
	// Running time : O(h) where h is the height of binary search tree
	public TreeNode treeSearch(TreeNode x, int k) {
		if(x == null || k == x.key) {
			return x;
		}
		if(k < x.key) {
			return treeSearch(x.left, k);
		}else {
			return treeSearch(x.right, k);
		}
	}
	
	public TreeNode maximum(TreeNode x) {
		while(x.right != null) {
			x = x.right;
		}
		return x;
	}
	
	public TreeNode minimum(TreeNode x) {
		while(x.left != null) {
			x = x.left;
		}
		return x;
	}
	
	// Running time : O(h) where h is the height of binary search tree
	public TreeNode successor(TreeNode x) {
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
	
	// Running time : O(h) where h is the height of binary search tree
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
	
	public void transplant(BinarySearchTree T, TreeNode u, TreeNode v) {
		if(u.parent == null) {
			T.root = v;
		}else if(u == u.parent.left) {
			u.parent.left = v;
		}else {
			u.parent.right = v;
		}
		if(v != null) {
			v.parent = u.parent;
		}
	}
	
	public void delete(BinarySearchTree T, TreeNode z) {
		if(z.left == null) {
			transplant(T, z, z.right);
		}else if(z.right == null) {
			transplant(T, z, z.left);
		}else {
			TreeNode y = minimum(z.right);
			if(y.parent != z) {
				transplant(T, y, y.right);
				y.right = z.right;
				y.right.parent = y;
			}
			transplant(T, z, y);
			y.left = z.left;
			y.left.parent = y;
		}
	}
}

public class BSearchTree{
	public static void main(String args[]) {
		TreeNode t1 = new TreeNode(1);
		TreeNode t2 = new TreeNode(6);
		BinarySearchTree tree = new BinarySearchTree();
		tree.insert(tree, new TreeNode(2));
		tree.insert(tree, new TreeNode(3));
		tree.insert(tree, new TreeNode(5));
		tree.insert(tree, new TreeNode(4));
		tree.insert(tree, t1);
		tree.insert(tree, t2);
		tree.transplant(tree, t1, t2);
		tree.inOrder(tree.root);
		tree.delete(tree, t1);
		System.out.println();
		tree.inOrder(tree.root);
	}
}
