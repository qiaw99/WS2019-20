__author__ = "Qianli Wang und Nazar Sopiha"
__copyright__ = "Copyright (c) 2019 qiaw99"
# https://github.com/qiaw99/WS2019-20/blob/master/LICENSE

import os
import sys
import numpy as np

class Logger(object):
	def __init__(self, filename = "daten.txt"):
		self.terminal = sys.stdout
		self.log = open(filename, "a")
 
	def write(self, message):
		self.terminal.write(message)
		self.log.write(message)

	def flush(self):
		pass

'''
	Komplexität = O(n)
	Speicherbedarf = O(n)
	Wir generieren eine globale Liste mit Zwischenergebnise, die mehrfach benutzt werden kann, 
	damit es reicht, factorial() nur einmal aufzurufen.
'''
def factorial(x):
	# Initialisierung
	global ls
	ls = [0 for i in range(x + 1)]

	if(x < 0):
		raise RuntimeError("Must be postive or 0!")
	else:
		ls[0] = 1
		if(x == 0):
			return ls[x]
		elif(x == 1):
			ls[1] = 1
			return ls[x]
		else:
			ls[1] = 1
			for i in range(2, x + 1):
				ls[i] = i * ls[i - 1]
		return ls[x]

def exp_approx(x, N):
	sum = 0
	# ls berechnen
	factorial(N)
	for k in range(N + 1):
		sum += x**k / ls[k]
	return sum

def g1(N, x):
	return exp_approx(x, N)

def g2(N, x):
	return 1 / exp_approx(-x, N)

def g3(N, x, K):
	temp = (abs(x) / float(K)) ** (np.sign(x) * K)
	return exp_approx(temp, N)

def error1(x, N):
	return abs(g1(N, x) - exp_approx(x, N)) / exp_approx(x, N)

def error2(x, N):
	return abs(g2(N, x) - exp_approx(x, N)) / exp_approx(x, N)

def error3(x, N, K):
	return abs(g3(N, x, K) - exp_approx(x, N)) / exp_approx(x, N)

def main():
	global x_seq, K_seq, N_seq, ls
	x_seq = [-5, 1, 5]
	K_seq = [1, 11]
	N_seq = [i for i in range(0, 51, 5)]	# length = 11

	path = os.path.abspath(os.path.dirname(__file__))
	type = sys.getfilesystemencoding()
	sys.stdout = Logger('daten.txt')

	for n in N_seq:

		print("	   x		n	err") 
		for x in x_seq:
			print("error1| ","%-5f|%-10f|%-10f|" %(x, n, error1(x, n)))
			print("error2| ","%-5f|%-10f|%-10f|" %(x, n, error2(x, n)))

		print("	    x	      n		k  	   err") 
		for x in x_seq:
			for k in K_seq:
				print("error3| ","%-5f|%-10f|%-10f|%-10f|" %(x, n, k, error3(x, n, k))) 

if __name__ == '__main__':
	main()

