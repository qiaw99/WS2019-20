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

def absoluteError(x,y):
	return abs(x - y)

def relativeError(x, errAbs):
	return errAbs / x

x = float(input("x ? \n"))
y = float(input("y ? \n"))
print(fixedpoint(x))
print("The absoluteError is: %.4f " %absoluteError(x,y))
print(round(relativeError(x, absoluteError(x,y)),4))
