__author__ = "Qianli Wang and Nazar Sopiha"
__copyright__ = "Copyright (c) 2019 qiaw99"
# https://github.com/qiaw99/WS2019-20/blob/master/LICENSE

def berechnen(g):
	# g = (a, value, b)
	# f(x) = g(x) * x + c 
	ls = []
 	# Erste Konstant
	temp = g[1]
	# Angenommen, dass c1 = 0
	ls.append(((g[0], temp * g[0]), (g[2], temp * g[2])))
	counter = 0
	for i in range(2, len(g) - 2, 2):
		k = g[i+1]
		y = ls[counter][1][1]
		x = g[i]
		c = y - x * k
		ls.append(((x, y), (g[i+2], k * g[i+2] + c)))
		counter += 1
	return ls

def auswerten(f, x):
	if(x < f[0][0][0] or x >= f[-1][1][0]):
		raise Exception("Out of range!")
	i = 0

	# i ist Index größer als x
	while(x > f[i][0][0]):
		if(i < len(f) - 1):
			i += 1
		else:
			i += 1
			break

	i -= 1

	# Ein Tupel, das 2 Punkte enthalt
	temp = f[i]
	print("In der Funktion: ", temp)
	x1 = temp[0][0]
	x2 = temp[1][0]
	y1 = temp[0][1]
	y2 = temp[1][1]
	k = float(y2-y1) / (x2 - x1)
	c = y1 - k * x1
	return k * x + c 

def test():
	print("###### Erster Teil: ######")
	print("###### Erstes Beispiel:")
	print("Die Funktion, die in lineare stückweise Funktion umgewandelt wird:")
	f = (1,2,3,4,5,6,7)
	print(f, "\n")
	print("Das Ergebnis: ", berechnen(f), "\n")

	print("###### Zweites Beispiel:")
	print("Die Funktion, die in lineare stückweise Funktion umgewandelt wird:")
	f = (1,4,5,9,7,19,20,43)
	print(f, "\n")
	print("Das Ergebnis: ", berechnen(f), "\n")

	print("###### Drittes Beispiel:")
	print("Die Funktion, die in lineare stückweise Funktion umgewandelt wird:")
	f = (-10,4,-5,8,3,16,2,14)
	print(f, "\n")
	print("Das Ergebnis: ", berechnen(f), "\n")

	print("###### Zweiter Teil: ######")
	print("Die geteste Funktion ist:", (((1, 2), (2, 3)), ((2, 3), (6, 10)), ((6, 10), (7, 8))),"\n")
	print("Der Wert an der Stelle 1.5: ", auswerten((((1, 2), (2, 3)), ((2, 3), (6, 10)), ((6, 10), (7, 8))), 1.5), "\n")
	print("Der Wert an der Stelle 4: ",auswerten((((1, 2), (2, 3)), ((2, 3), (6, 10)), ((6, 10), (7, 8))), 4), "\n")
	print("Der Wert an der Stelle 6.3: ",auswerten((((1, 2), (2, 3)), ((2, 3), (6, 10)), ((6, 10), (7, 8))), 6.3), "\n")

def main():
	test()

if __name__ == '__main__':
	main()
