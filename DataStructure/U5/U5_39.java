import java.util.ArrayList;

/**
 *  Author: Qianli Wang and Nazar Sopiha
 */

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
        test();
    }

    public static void test(){
        System.out.println("Das erste Beispiel mit der Eingabeliste {1, 2, 3, 4, 5, 6}");
        int[] arr1 = new int[] {1,2,3,4,5,6};
        BinarySearchTree tree1 = transform(arr1);
        System.out.println("Das Ergebnis: " + tree1.getTotal());
        System.out.println();

        System.out.println("Das zweite Beispiel mit der Eingabeliste {10, 12, 4, 8, 1}");
        int[] arr2 = new int[] {10,12,4,8,1};
        BinarySearchTree tree2 = transform(arr2);
        System.out.println("Das Ergebnis: " + tree2.getTotal());
        System.out.println();

        System.out.println("Das erste Beispiel mit der Eingabeliste {20, 12, 50, 4, 5, 2, 6, 29, -12}");
        int[] arr3 = new int[] {20, 12, 50, 4, 5, 2, 6, 29, -12};
        BinarySearchTree tree3 = transform(arr3);
        System.out.println("Das Ergebnis: " + tree3.getTotal());
    }

    public static BinarySearchTree transform(int [] arr){
        BinarySearchTree tree = new BinarySearchTree();
        for(int i = 0; i < arr.length; i++){
                tree.insert(tree, new TreeNode(arr[i]));
        }
        return tree;
    }
}
