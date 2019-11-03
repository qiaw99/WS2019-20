'''
import pysnooper
@pysnooper.snoop()
'''
__author__ = "Qianli und Nazar"
__copyright__ = "Copyright (c) 2019 qiaw99"
# https://github.com/qiaw99/WS2019-20/blob/master/LICENSE

import numpy as np
import math
from matplotlib import pyplot as plt

def plotGraphic():
	'''
	# Aufgabe 4 a)
	x = np.arange(0, 2 * math.pi + 1, 0.01)
	y = np.sin(x)
	plt.title("Plot der Sinusfunktion")
	plt.xlabel("x axis caption")
	plt.ylabel("y axis caption")
	plt.plot(x, y)
	plt.savefig("plot1.png")
	# Have to call savefig() before show(),
	# because when we call show(), a new page
	# will be produced.
	plt.show()

	# Aufgabe 4 b)
	x = np.arange(0, 11, 0.1)
	y = np.floor(x)
	plt.title("Plot der floorfunktion")
	plt.xlabel("x axis caption")
	plt.ylabel("y axis caption")
	plt.plot(x, y, "ob")
	plt.savefig("plot2.png")
	plt.show()

	# Aufgabe 4 c)
	x = np.arange(0, 11)
	y = x * x
	plt.title("Plot der Funktion mit skalierten Achsen")
	plt.xlabel("x axis caption")
	plt.ylabel("y axis caption")
	plt.loglog(x, y, basex = 2, basey = 2)
	plt.savefig("plot3.png")
	plt.show()
	'''

	# Aufgabe 4 d)
	x = np.arange(0, 2 * math.pi + 1, 0.01)
	y1 = np.sin(x)
	# ha = "left"
	plt.title("Plot der Funktion mit skalierten Achsen")

	plt.subplot(1, 1, 1)
	plt.plot(x, y1, color = 'r', label = "sin x")

	y2 = np.cos(x)
	plt.plot(x, y2, 'b', label = "cos x") 

	y3 = 1 / np.square(math.pi) * x * (2 * math.pi - x)
	plt.plot(x, y3, color = 'y', label = r"$\frac{1}{π^2}x(2π−x)$")
	plt.legend(loc = 'upper right')
	plt.savefig("plot4.png")
	plt.show()

def main():
	plotGraphic()

if(__name__ == '__main__'):
	main()
