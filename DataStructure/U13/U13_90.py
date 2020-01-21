#-*- coding:utf-8 -*-

import six
import sys

# Abstract class
class HuffNode(object):
    def get_weight(self):
        raise NotImplementedError(
            "The Abstract Node Class doesn't define 'get_weight'")

    def isleaf(self):
        raise NotImplementedError(
            "The Abstract Node Class doesn't define 'isleaf'")

class LeafNode(HuffNode):
    def __init__(self, value = 0, freq = 0,):
        super(LeafNode, self).__init__()
        self.value = value
        self.weight = freq
        
    def isleaf(self):
        return True

    def get_weight(self):
        return self.weight

    def get_value(self):
        return self.value

# Class of nodes in the middle
class IntNode(HuffNode):
    def __init__(self, left_child = None, right_child = None):
        super(IntNode, self).__init__()
        self.weight = left_child.get_weight() + right_child.get_weight()
        self.left_child = left_child
        self.right_child = right_child

    def isleaf(self):
        return False

    def get_weight(self):
        return self.weight

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child

class HuffTree(object):
    def __init__(self, flag, value = 0, freq = 0, left_tree = None, right_tree = None):
        super(HuffTree, self).__init__()
        if flag == 0:
            self.root = LeafNode(value, freq)
        else:
            self.root = IntNode(left_tree.get_root(), right_tree.get_root())

    def get_root(self):
        return self.root

    def get_weight(self):
        return self.root.get_weight()

    def traverse_huffman_tree(self, root, code, char_freq):
        """
        Traverse the huffman tree so that we can get every huffman codings 
        corresponded each character and store in char_freq
        """
        if root.isleaf():
            char_freq[root.get_value()] = code
            print(("it = %c  and  freq = %d  code = %s") %(chr(root.get_value()), root.get_weight(), code))
            return None
        else:
            self.traverse_huffman_tree(root.get_left(), code + '0', char_freq)
            self.traverse_huffman_tree(root.get_right(), code + '1', char_freq)

def buildHuffmanTree(list_hufftrees):
    while len(list_hufftrees) > 1:
        # sort the list according to the weight
        list_hufftrees.sort(key = lambda x: x.get_weight()) 
               
        # choose two of the smallest nodes and slice the list_hufftrees
        temp1 = list_hufftrees[0]
        temp2 = list_hufftrees[1]
        list_hufftrees = list_hufftrees[2:]

        # construct a new HuffTree
        list_hufftrees.append(HuffTree(1, 0, 0, temp1, temp2))
    return list_hufftrees[0]

def compress(inputfilename, outputfilename):
    f = open(inputfilename,'rb')
    filedata = f.read()
    filesize = f.tell()

    # count the times that a character has shown
    char_freq = {}
    for x in range(filesize):
        temp = filedata[x] 
        if temp in char_freq.keys():
            char_freq[temp] += 1
        else:
            char_freq[temp] = 1
    """
    for temp in char_freq.keys():
        print(temp,': ',char_freq[temp])
    """
    # construct the hufftree list to build the tree
    list_hufftrees = []
    for x in char_freq.keys():
        list_hufftrees.append(HuffTree(0, x, char_freq[x], None, None))
        
    length = len(char_freq.keys())
    output = open(outputfilename, 'wb')

    # An integer has 4 bytes
    a4 = length & 255
    length = length >> 8
    a3 = length & 255
    length = length >> 8
    a2 = length & 255
    length = length >> 8
    a1 = length & 255
    output.write(six.int2byte(a1))
    output.write(six.int2byte(a2))
    output.write(six.int2byte(a3))
    output.write(six.int2byte(a4))

    # traverse the dictionary and write all values and frequencies
    for x in char_freq.keys():
        output.write(six.int2byte(x))
        temp = char_freq[x]
        a4 = temp & 255
        temp = temp >> 8
        a3 = temp & 255
        temp = temp >> 8
        a2 = temp & 255
        temp = temp >> 8
        a1 = temp& 255
        # convert an integer to byte
        output.write(six.int2byte(a1))
        output.write(six.int2byte(a2))
        output.write(six.int2byte(a3))
        output.write(six.int2byte(a4))
    
    temp = buildHuffmanTree(list_hufftrees)
    temp.traverse_huffman_tree(temp.get_root(), '', char_freq)
