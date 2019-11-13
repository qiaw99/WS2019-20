import java.util.*;
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
        public static ArrayList<TreeNode> nodeList;

        public BinarySearchTree(){
                root = null;
                nodes = 0;
                nodeList = new ArrayList<TreeNode>();
        }

        public float getTotal(){
                float total = 0;
                for (TreeNode i : nodeList) {
                    total += getInternalLength(i);
                }
                return total / this.getSize();

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
                        System.out.println("Key of element is: " + n.key);
                        n = n.parent;
                }
                return counter;
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
                nodeList.add(z);
        }
}

public class U5_39{
        public static void main(String args[]){
                int[] arr = new int []{10,12,4,8,1};
                BinarySearchTree tree = transform(arr);
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
