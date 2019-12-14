import numpy as np
import math
from matplotlib import pyplot as plt
# n*d*logd(n)+(m+n)logd(n)

# m = n
x = np.arange(0, 10000)
n = 10
y = math.log(n, x) * d * n + 2*n*math.log(n,d)
plt.title("Plot der Sinusfunktion")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption")
plt.plot(x, y)
plt.show()
