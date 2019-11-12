def berechnen(g):
	# g = (a, value, b)
	# f(x) = g(x) * x + c 
	ls = []
	value = g[1]
	def calculate_fx(x):
		return value * x
	ls.append((g[0], calculate_fx(g[0])))
	ls.append((g[2], calculate_fx(g[2])))
	ls = tuple(ls)
	return ls

def auswerten(f, x):
	first = f[0][0]
	second = f[1][0]
	if(x < first or x >= second):
		raise Exception("Out of range!")
	first_value = f[0][1]
	second_value = f[1][1]
	k = float(second_value - first_value) / (second - first)
	b = first_value - k * first
	return x * k + b


def main():
	print("##########Berechnen eine Darstellung von f aus g:##########")
	g = eval(input("Wie ist der Wert von g?\n"))
	print("a = ", g[0], " b = ", g[2])
	print("f(x) = ", g[1], "*x")
	print("f(x) ist: ",berechnen(g))
	
	print("##########Auswertung einer Funktion an der Stelle x:##########")
	f = eval(input("Geben Sie eine lineare Funktion ein.\n"))
	temp = int(input("An welcher Stelle? \n"))
	print("Auswertung an ", temp, " = ", auswerten(f, temp))

if __name__ == '__main__':
	main()
