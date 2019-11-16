class RBTreeNode{
	public int key;
	public RBTreeNode left, right, parent = null;
	public String color;
	public int size;

	public RBTreeNode(int key){
		this.key = key;
		this.color = "black";
	}
}

class RBTree{
	public RBTreeNode root, nil;

	public RBTree(){
		nil = new RBTreeNode(0);
		root = nil;
	} 

	public void preOrder(RBTreeNode n){
		if(n != null){
			System.out.println("The key is: " + n.key + " , the color is: " + n.color);
			preOrder(n.left);
			preOrder(n.right);
		}
	}

	public void leftRotate(RBTreeNode x){
		RBTreeNode y = x.right;
		x.right = y.left;
		if(y.left != nil)
			y.left.parent = x;

		// Set the relation between y and its parent
		y.parent = x.parent;
		if(x.parent == nil)
			root = y;
		else if(x.parent.left == x)
			x.parent.left = y;
		else
			x.parent.right = y;

		y.left = x;
		x.parent = y;
	}

	public void rightRotate(RBTreeNode x){
		RBTreeNode y = x.left; 
		x.left = y.right; 
		if(y.right != nil)
			y.right.parent = x;
		y.parent = x.parent;
		if(x.parent == nil)
			root = y;
		else if(x.parent.left == x)
			x.parent.left = y;
		else
			x.parent.right = y;
		y.right = x;
		x.parent = y;
	}

	public String RBInsert(RBTreeNode z){
		RBTreeNode x, y;
		y = nil;
		x = root;
		while(x != nil){
			y = x;
			if(z.key < x.key){
				x = x.left;
			}else{
				x = x.right;
			}
		}
		z.parent = y;
		if(y == nil){
			root = z;
		}else if(z.key < y.key){
			y.left = z;
		}else{
			y.right = z;
		}
		z.left = nil;
		z.right = nil;
		z.color = "red";
		RBInsertFixUp(z);
		return "Inserted key is: " + z.key + ", color: " + z.color;
	}

	public void RBInsertFixUp(RBTreeNode z){
		while(z.parent.color == "red"){
			if(z.parent == z.parent.parent.left){
				RBTreeNode y = z.parent.parent.right;
				// Case 1
				if(y.color == "red"){
					z.parent.color = "black";
					y.color = "black";
					z.parent.parent.color = "red";
					z = z.parent.parent;
				}else if(z == z.parent.right){
					// Case 2
					z = z.parent;
					leftRotate(z);
				}else{
					// Case 3
					z.parent.color = "black";
					z.parent.parent.color = "red";
					rightRotate(z.parent.parent);
				}
			}else{
				RBTreeNode y = z.parent.parent.left;
				if(y.color == "red"){
					z.parent.color = "black";
					y.color = "black";
					z.parent.parent.color = "red";
					z = z.parent.parent;
				}else if(z == z.parent.left){
					z = z.parent;
					leftRotate(z);
				}else{
					z.parent.color = "black";
					z.parent.parent.color = "red";
					rightRotate(z.parent.parent);
				}
			}
		}
		root.color = "black";
	}

	public void RBTransplant(RBTreeNode u, RBTreeNode v){
		if(u.parent == nil){
			root = v;
		}else if(u == u.parent.left){
			u.parent.left = v;
		}else{
			u.parent.right = v;
		}
		v.parent = u.parent;
	}

	public RBTreeNode minimum(RBTreeNode n){
		while(n != nil){
			n = n.left;
		}
		return n;
	}
	public void RBDelete(RBTreeNode z){
		RBTreeNode y = z; 
		RBTreeNode x;
		String y_original_color = y.color; 
		// If z has just one child
		if(z.left == nil){
			x = z.right;
			RBTransplant(z, z.right);
		}else if(z.right == nil){
			x = z.left;
			RBTransplant(z, z.left);
		}else{
			y = minimum(z.right);
			y_original_color = y.color; 
			x = y.right;
			if(y.parent == z)
				x.parent = y;
			else{
				// y.right substitutes the position of y 
				RBTransplant(y, y.right);
				y.right = z.right;
				y.right.parent = y;
			}
			RBTransplant(z, y);
			y.left = z.left;
			y.left.parent = y;
			y.color = z.color ;
		}	
		/**
		1. The black height doesn't change
		2. if y is red, then y cannot be the root. So the color of root is still black
		3. There are no 2 red nodes in neighbor
		*/
		if(y_original_color == "black")
			RBDeleteFixUp(x);
	}

	public void RBDeleteFixUp(RBTreeNode x){
		while(x != root && x.color == "black"){
			RBTreeNode w;
			if(x == x.parent.left){
				w = x.parent.right;
				if(w.color == "red"){
					w.color = "black";
					x.parent.color = "red";
					leftRotate(x.parent);
					w = x.parent.right;
				}
				if(w.left.color == "black" && w.right.color =="black"){
					w.color = "red";
					x = x.parent;
				}else if(w.right.color == "black"){
					w.left.color = "black";
					w.color = "red";
					rightRotate(w);
					w = x.parent.right;
				}else{
					w.color = x.parent.color; 
					x.parent.color = "black";
					w.right.color = "black";
					leftRotate(x.parent);
					x = root;
				}
			}else{
				w = x.parent.left;
				if(w.color == "red"){
					w.color = "black";
					x.parent.color = "red";
					rightRotate(x.parent);
					w = x.parent.left;
				}
				if(w.right.color == "black" && w.left.color =="black"){
					w.color = "red";
					x = x.parent;
				}else if(w.left.color == "black"){
					w.right.color = "black";
					w.color = "red";
					leftRotate(w);
					w = x.parent.left;
				}else{
					w.color = x.parent.color; 
					x.parent.color = "black";
					w.left.color = "black";
					rightRotate(x.parent);
					x = root;
				}
			}
		}
		x.color = "black";
	}
}

public class RedBlackTree{
	public static void main(String args[]){
		RBTree tree = new RBTree();
		for(int i = 10; i > 0; i--){
			tree.RBInsert(new RBTreeNode(i));
		}
		tree.preOrder(tree.root);
	}
}
