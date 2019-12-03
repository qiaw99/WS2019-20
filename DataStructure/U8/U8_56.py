import os
import sys

class Logger(object):
	def __init__(self, filename = "daten.txt"):
		self.terminal = sys.stdout
		self.log = open(filename, "a")
 
	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)

	def flush(self):
		pass
        
path = os.path.abspath(os.path.dirname(__file__))
type = sys.getfilesystemencoding()
sys.stdout = Logger('daten.txt')        

for i in range(1,7):
    for j in range(1,7):
        if(i<j):
            print(i,j,3**(j-i))
        elif(i>j):
            print(i,j,i-j)
        else:
            pass
