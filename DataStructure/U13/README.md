# Compress and depress files:
While compressing, we have to shore how many leaves do we have and also the Huffman codes which create the Huffman tree. Also, it's important to take care of last bits of file. Because it's quite possible that there are less than 8 bits. However, it's required while writing file in binary to fill the string with '0' so that the size of rest string equals 8bit.

For the process--decompress we could say, it's reversed process of compressing. Firstly, we read how many leaves do we have and also the Huffman tree, with help of which we can reconstruct the Huffman tree. 
