import math
import sys
import os

f1 = lambda x : x * (x + 2)
f2 = lambda x : math.sqrt(x + 1) - 1

def concat(f1,f2):
	return lambda x : f1(f2(x))

def generateData(x):
	h = concat(f2,f1)	# f^(-1) * f
	g = concat(f1,f2)
	val1 = h(x)
	err1 = abs(val1 - x)
	val2 = g(x)
	err2 = abs(val2 - x)
	return (val1, val2, err1, err2)
 
class Logger(object):
    def __init__(self, filename="daten.txt"):
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
 
print(path)
print(os.path.dirname(__file__))
for i in range(13):
	tp = generateData(-1 + 10**(-i))
    print("%-2i",%i)
    #print("%-2i%-12f%-12f%-12f%-12f" %(i, tp[0],tp[1],tp[2],tp[3]))
    
print('------------------')
