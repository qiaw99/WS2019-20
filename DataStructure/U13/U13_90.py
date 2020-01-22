#-*- coding:utf-8 -*-
__author__ = "Qianli Wang und Nazar Sopiha"
__copyright__ = "Copyright (c) 2019 qiaw99"
# https://github.com/qiaw99/WS2019-20/blob/master/LICENSE

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
        Traverse the Huffman tree so that we can get every huffman codings 
        corresponded each character and store in char_freq
        """
        if root.isleaf():
            char_freq[root.get_value()] = code
            print(("item = %c  and  freq = %d  code = %s") %(chr(root.get_value()), root.get_weight(), code))
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
    # construct the Huffman tree list to build the tree
    list_hufftrees = []
    for x in char_freq.keys():
        list_hufftrees.append(HuffTree(0, x, char_freq[x], None, None))
        
    length = len(char_freq.keys())
    output = open(outputfilename, 'wb')

    
    # An integer has 4 bytes, the number of keys
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
    # the coding must be stored for decompress
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
    
    # traverse the whole file and generate the Huffman coding
    code = ''
    for i in range(filesize):
        key = filedata[i] 
        code = code + char_freq[key]
        out = 0
        while len(code) > 8:
            for x in range(8):
                out = out << 1
                if code[x] == '1':
                    out |= 1
            code = code[8:]
            output.write(six.int2byte(out))
            out = 0

    # the coding less than 8 bits
    # the number of leaves
    output.write(six.int2byte(len(code)))
    out = 0
    for i in range(len(code)):
        out <<= 1
        if code[i] == '1':
            out = out|1
    for i in range(8 - len(code)):
        out <<= 1
    output.write(six.int2byte(out))

    output.close()

def decompress(inputfilename, outputfilename):
    f = open(inputfilename,'rb')
    filedata = f.read()
    filesize = f.tell()

    # An integer, the number of leaves
    a1 = filedata[0]
    a2 = filedata[1]
    a3 = filedata[2]
    a4 = filedata[3]    
    j = 0
    j = j | a1
    j = j << 8
    j = j | a2
    j = j << 8
    j = j | a3
    j = j << 8
    j = j | a4

    leaf_node_size = j

    # put all frequencies and keys into the dictionary
    char_freq = {}
    for i in range(leaf_node_size):
        c = filedata[4 + i * 5]
        
        a1 = filedata[4 + i * 5 + 1]
        a2 = filedata[4 + i * 5 + 2]
        a3 = filedata[4 + i * 5 + 3]
        a4 = filedata[4 + i * 5 + 4]
        j = 0
        j = j | a1
        j = j << 8
        j = j | a2
        j = j << 8
        j = j | a3
        j = j << 8
        j = j | a4
        print(c, j)
        char_freq[c] = j

    # reconstruct the Huffman tree
    list_hufftrees = []
    for x in char_freq.keys():
        list_hufftrees.append(HuffTree(0, x, char_freq[x], None, None))

    temp = buildHuffmanTree(list_hufftrees)
    temp.traverse_huffman_tree(temp.get_root(), '', char_freq)

    # decompress according to the Huffman tree
    output = open(outputfilename, 'wb')
    code = ''
    currnode = temp.get_root()
    for x in range(leaf_node_size * 5 + 4, filesize):
        c = filedata[x]
        for i in range(8):
            if c & 128:
                code = code +'1'
            else:
                code = code + '0'
            c <<= 1

        while len(code) > 24:
            if currnode.isleaf():
                temp_byte = six.int2byte(currnode.get_value())
                output.write(temp_byte)
                currnode = temp.get_root()

            if code[0] == '1':
                currnode = currnode.get_right()
            else:
                currnode = currnode.get_left()
            code = code[1:]


    # Handle the last 24 bits
    sub_code = code[-16: -8]
    last_length = 0
    for i in range(8):
        last_length <<= 1
        if sub_code[i] == '1':
            last_length |= 1

    code = code[:-16] + code[-8:-8 + last_length]

    while len(code) > 0:
            if currnode.isleaf():
                temp_byte = six.int2byte(currnode.get_value())
                output.write(temp_byte)
                currnode = temp.get_root()

            if code[0] == '1':
                currnode = currnode.get_right()
            else:
                currnode = currnode.get_left()
            code = code[1:]

    if currnode.isleaf():
        temp_byte = six.int2byte(currnode.get_value())
        output.write(temp_byte)
        currnode = temp.get_root()

    output.close()

if __name__ == '__main__':
    # FLAG 0 compress 1 decompress
    # INPUTFILE： input filename
    # OUTPUTFILE：output filename
    if len(sys.argv) != 4:
        print("The number of input is wrong!")
        print("The first parameter is filename")
        print("The second parameter is flag: 0-compress, 1-decompress")
        print("The third parameter is inputfilename")
        print("The forth parameter is outputfilename")
        exit(0)
    else:
        FLAG = sys.argv[1]
        INPUTFILE = sys.argv[2]
        OUTPUTFILE = sys.argv[3]

    if FLAG == '0':
        print('Compress file:')
        compress(INPUTFILE,OUTPUTFILE)
    else:
        print('Decompress file:')
        decompress(INPUTFILE,OUTPUTFILE)
