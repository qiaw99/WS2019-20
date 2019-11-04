'''
import pysnooper
@pysnooper.snoop()
'''
__author__ = "Qianli und Nazar"
__copyright__ = "Copyright (c) 2019 qiaw99"
# https://github.com/qiaw99/WS2019-20/blob/master/LICENSE

# Aufgabe 3 a)
def fixedpoint(x):
	temp = str(x)
	result = None

	# Check whether there is a coma in the input
	if('.' in temp):
		# Get the index of '.'
		xIndex = temp.index('.')

		# Copy all the numbers before '.'
		y = temp[0:xIndex + 1]
		if(len(temp) - 1 - xIndex >= 2):
			first = temp[xIndex + 1]
			second = temp[xIndex + 2]
			if(second >= '5'):
				first = int(first)
				# Check the negative number
				if(temp[0] == '-'):
					pass
				else:
					first += 1
				first = str(first)
				return float(y + first)
			else:
				return float(y + first)	
		else:
			return float(temp)
	else:
		return float(temp + '.0')

# Aufgabe 3 b)
def absoluteError(x,y):
	return abs(x - y)

# # Aufgabe 3 c)
def relativeError(x, errAbs):
	return errAbs / x

def test():
	x = float(input("The exact number? \n"))
	y = float(input("The actual number? \n"))
	print("The result of fixed point is: " + str(fixedpoint(x)))
	print("The absoluteError is: %.2f " %absoluteError(x,y))
	print("The relative error is: %.2f" %relativeError(x, absoluteError(x,y)))

def main():
	test()

if (__name__ == '__main__'):
	main()
