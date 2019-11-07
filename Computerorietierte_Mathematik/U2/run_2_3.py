from test import *

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

# # Aufgabe 3d)
def fill_src_arr (X):
    for i in range (1 ,100002):   #first value is 0.001, goes till (upper bound - 1)
        X.append(i/1000)
    return X
    
def fill_abs_arr(src, abs_err):
    for i in range (100001):
        rounded_num = fixedpoint(src[i])
        abs_error = absoluteError(src[i], rounded_num)
        abs_err.append(abs_error)
    return abs_err
    
def fill_rel_arr(src, abs_err, rel_err):
    for i in range (100001):
        rel_error = relativeError(src[i], abs_err[i])
        rel_err.append(rel_error)
    return rel_err
    
def print_err():
    src = []     #source array
    abs_err = [] # array of absoulte errors
    rel_err = [] # array of relative errors
    fill_src_arr(src)
    print(src[2])
    fill_abs_arr(src, abs_err)
    print(abs_err[2])
    fill_rel_arr(src, abs_err, rel_err)
    print(rel_err[2])
    for i in range (100):
        print("source: ", src[i], "value:", fixedpoint(src[i]), "abs: ", abs_err[i], "rel: ", rel_err[i]) # just for test
    plotErrors(src, abs_err, rel_err)
    
print_err()
    
