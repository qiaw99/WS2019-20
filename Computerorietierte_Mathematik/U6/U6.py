import math
from tabulate import tabulate

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

temp = []
for i in range(13):
	ls = list(generateData(-1 + 10**(-i)))
	tmep.append(ls)
