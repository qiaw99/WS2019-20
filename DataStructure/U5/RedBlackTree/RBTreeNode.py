class RBTreeNode(object):
	def __init__(self, x):
		self.key = x
		self.left = None
		self.right = None
		self.parent = None
		self.color = "black" 
		self.size = None
