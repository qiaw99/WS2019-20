# Aufgabe 2 a)
def runden(x, l):
	print(x)
	x = str(x)
	# In the input there is '\n' whose length equal 2
	print("len" + 	str(len(x)-1))
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
					print("return x")
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
	return rd(x + y, length)

def my_mult(x, y, rd):
	temp = x * y
	print("temp:", temp)
	return rd(temp, length)

def binomA(a, b, rd):
	a = float(rd(a, length))
	b = float(rd(b, length))
	print('a= ',end='')
	print(a)
	print('b= ',end='')
	print(b)
	return my_add(a, b, length)
	

global length 
length = 5

print(my_add(2.0,3.0,runden))


