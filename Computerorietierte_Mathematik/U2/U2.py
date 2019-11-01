import numpy as np
import math
from matplotlib import pyplot as plt

def plotGraphic():
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


plotGraphic()
