# AVL trees
__Balanced or not__ :
h = lg(n)

h is the height of BST = length of longest path from root down to leaf.

The tree is balanced if h = Θ(lg n)

----
__Height of a node in the tree :__
Length of longest path from it down to a leaf. 

Height = max{ height(left child), height(right child) } + 1

Define: the height of a leaf is -1.

----
__AVL trees :__
Require heights of left and right children of every node to differ by at most 1 or -1.

=>	|height(left) – height(right)| <= 1

AVL trees are balanced.

Worst case is when right(left) subtree has height 1 more than left(right) for every node.

Define N(h) = min # nodes in a AVL tree of height h. 

N(h) = 1 + N(h-1) + N(h -2)	(h < 1.440 lgn)

 > 1 + 2N(h -2)

 > 2N(h - 2)

= Θ(2 ^ (n/2))

h < 2 lgn

----
__AVL insert :__
1)	Simple BST insert
2)	Fix AVL property

#### From changed node up
-	Suppose x Is lowest node violating AVL.
-	Assume right (x) higher
-	If x’s right child is right-heavy or balanced 
-	Else: like zig-zag have to rotate twice.

Rotations :
O(1) time
     
----     
__AVL sort:__
-	Insert n items          ->Θ(nlgn)
-	In-order traversal      ->Θ(n)

----
__Abstract Data Type:__
-	Insert & delete
-	Min
-	Successor/pred			

with 1) and 2) is priority queue.

with 1), 2) and 3) is balanced tree.

----
__Data Structure__
-	Heap ->AVL

