import math

def concat(f,g,x):
	return f1(f2(x))

def f1(x):
	if(x >= -1):
		y = x * (x + 2)
		if(y >= -1):
			return y
		else:
			raise Exception("y is out of range!")
	else:
		raise Exception("x is out of range!")

def f2(x):
	if(x >= -1):
		y = math.sqrt(x + 1) - 1
		if(y >= -1):
			return y
		else:
			Exception("y is out of range!")
	else:
		raise Exception("x is out of range!")

def generateData(x):
	val1 = concat(f2,f1,x)
	err1 = abs(val1 - x)
	val2 = concat(f1,f2,x)
	err2 = abs(val2 - x)
	#return (val1, val2, err1, err2)
	return val1 == val2

for i in range(13):
	print(generateData(-1 + 10**(-i)))
