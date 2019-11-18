# Aufgabe 2 a)
def runden(x, l):
	#changing presentation of x for the cases, when x is something like 4.9999999999991343e-06. Using precision of 20 digits
	u = ('{:.20f}'.format(x))
	x = str(u)
	# In the input there is '\n' whose length equal 2
	if(x[0] == '-'):
		if(not '.' in x):
			if(len(x) - 2 > l):
				raise Exception("l is too small!")
			elif(len(x) - 2 == l):
				return x
			else:
				return x + '.' + '0' * (l - len(x) + 1)
		else:
			if(x.index('.') - 1 > l):
				raise Exception("l ist zu klein. Ein Integer kann auch nicht dargestellt werden.")
			elif(x.index('.') - 1 == l):
				if(int(x[x.index('.') + 1]) >= 5):
					return str(int(x[:x.index('.')]) - 1)
				else:
					return x[:x.index('.')]
			else:
				if(l > len(x) - 2):
					return (x + (l - len(x) + 2) * '0')
				elif(l == len(x) - 2):
					return x
				else:
					temp = int(x[l + 1])
					carry = x[l + 2]
					if(int(carry) >= 5):
						temp += 1
					else:
						pass
					return (x[0 : l+1] + str(temp))
	else:
		if('.' in x):
			if(x.index('.') > l):
				raise Exception(" hierl ist zu klein. Ein Integer kann auch nicht dargestellt werden.")
			elif(x.index('.') == l):
				if(int(x[x.index('.') + 1]) >= 5):
					return str(int(x[:x.index('.')]) + 1)
				else:
					return x[:x.index('.')]
			else:
				# len(x) - 1 is the length of number 
				if(l > len(x) - 1):
					return (x + (l - len(x) + 1) * '0')
				elif(l == len(x) -1):
					return x
				else:
					temp = int(x[l])
					carry = x[l + 1]
					if(int(carry) >= 5):
						temp += 1
					else:
						pass
					return (x[0:l] + str(temp))
		else:
			if(len(x) - 1 > l):
				raise Exception("l is too small!")
			elif(len(x) - 1 == l):
				return x
			else:
				return x + '.' + '0' * (l - len(x))

# Aufgabe 2 b) 
def my_add(x, y, rd):
	return float(runden(x + y, length))

def my_mult(x, y, rd):
	temp = x * y
	return float(runden(temp, length))

def binomA(a, b, rd):
	a = float(rd(a, length))
	b = float(rd(b, length))
	return my_mult(my_add(a, b, runden), my_add(a, b, runden), length)
	
def binomB(a, b, rd):	
	first = my_mult(float(runden(a, length)), float(runden(a, length)), length)
	second = 2 * my_mult(float(runden(a, length)), float(runden(b, length)), length)
	last = my_mult(float(runden(b, length)), float(runden(b, length)), length)
	return first + second + last

def main():
	global length 
	length = 7
	print(binomA(0.012345,-0.01234,runden))
	print(binomB(0.012345,-0.01234,runden))

if (__name__ == '__main__'):
	main()

