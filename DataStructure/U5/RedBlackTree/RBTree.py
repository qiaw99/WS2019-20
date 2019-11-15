from RBTreeNode import *

class RBTree(object):
	def __init__(self):
		# The Leaf
		self.nil = RBTreeNode(0)
		self.root = self.nil

	def leftRotate(T, x):
		y = x.right
		x.right = y.left
		if(y.left != T.nil):
			y.left.parent = x

		# Set the relation between y and its parent
		y.parent = x.parent
		if(x.parent == T.nil):
			T.root = y
		elif(x.parent.left == x):
			x.parent.left = y
		else:
			x.parent.right = y

		y.left = x
		x.parent = y

	def rightRotate(T, x):
		y = x.left 
		x.left = y.right 
		if(y.right != T.nil):
			y.right.parent = x
		y.parent = x.parent
		if(x.parent == T.nil):
			T.root = y
		elif(x.parent.left == x):
			x.parent.left = y
		else:
			x.parent.right = y
		y.right = x
		x.parent = y

	def RBInsert(T, z):
		y = T.nil
		x = T.root
		# Find the suitable position to insert
		while(x != T.nil):
			y = x
			if(z.key < x.key):
				x = x.left
			else:
				x = x.right
		z.parent = y
		if(y == T.nil):
			T.root = z
		elif(z.key < y.key):
			y.left = z
		else:
			y.right = z
		z.left = T.nil
		z.right = T.nil
		z.color = "red"
		RBInsertFixUp(T, z)
		return z.key, ", the color is: ", z.color

	def RBInsertFixUp(T, z):
		while(z.parent.color == "red"):
			if(z.parent == z.parent.parent.left):
				y = z.parent.parent.right
				# Case 1
				if(y.color == "red"):
					z.parent.color = "black"
					y.color = "black"
					z.parent.parent.color = "red"
					z = z.parent.parent
				# Case 2
				elif(z == z.parent.right):
					z = z.parent
					leftRotate(T, z)
				# Case 3	
				else:
					z.parent.color = "black"
					z.parent.parent.color = "red"
					rightRotate(T, z.parent.parent)
			else:
				y = z.parent.parent.left
				if(y.color == "red"):
					z.parent.color = "black"
					y.color = "black"
					z.parent.parent.color = "red"
					z = z.parent.parent
				elif(z == z.parent.left):
					z = z.parent
					leftRotate(T, z)
				else:
					z.parent.color = "black"
					z.parent.parent.color = "red"
					rightRotate(T, z.parent.parent)
		T.root.color = "black"		

	def RBTransplant(T, u, v):
		if(u.parent == T.nil):
			T.root = v
		elif(u == u.parent.left):
			u.parent.left = v
		else:
			u.parent.right = right
		v.parent = u.parent 

	def TreeMinimum(root):
		while(root.left != T.nil):
			root = root.left
		return root

	def RBDelete(T, z):
		y = z 
		y_original_color = y.color 
		# If z has just one child
		if(z.left == T.nil):
			x = z.right
			RBTransplant(T, z, z.right)
		elif(z.right == T.nil):
			x = z.left
			RBTransplant(T, z, z.left)
		else:
			y = TreeMinimum(z.right)
			y_original_color = y.color 
			x = y.right
			if(y.parent == z):
				x.parent = y
			else:
				# y.right substitutes the position of y 
				RBTransplant(T, y, y.right)
				y.right = z.right
				r.right.parent = y
			RBTransplant(T, z, y)
			y.left = z.left
			y.left.parent = y
			y.color = z.color 

		"""
		1. The black height doesn't change
		2. if y is red, then y cannot be the root. So the color of root is still black
		3. There are no 2 red nodes in neighbor
		"""
		if(y_original_color == "black"):
			RBDeleteFixUp(T, x)

	def RBDeleteFixUp(T, x):
		while(x != T.root and x.color == "black"):
			if(x == x.parent.left):
				w = x.parent.right
				if(w.color == "red"):
					w.color = "black"
					x.parent.color = "red"
					leftRotate(T, x.parent)
					w = x.parent.right
				if(w.left.color == "black" and w.right.color =="black"):
					w.color = "red"
					x = x.parent
				elif(w.right.color == "black"):
					w.left.color = "black"
					w.color = "red"
					rightRotate(T, w)
					w = x.parent.right
				else:
					w.color = x.parent.color 
					x.parent.color = "black"
					w.right.color = "black"
					leftRotate(T, x.parent)
					x = T.root
			else:
				w = x.parent.left
				if(w.color == "red"):
					w.color = "black"
					x.parent.color = "red"
					rightRotate(T, x.parent)
					w = x.parent.left
				if(w.right.color == "black" and w.left.color =="black"):
					w.color = "red"
					x = x.parent
				elif(w.left.color == "black"):
					w.right.color = "black"
					w.color = "red"
					leftRotate(T, w)
					w = x.parent.left
				else:
					w.color = x.parent.color 
					x.parent.color = "black"
					w.left.color = "black"
					rightRotate(T, x.parent)
					x = T.root
		x.color = "black"

