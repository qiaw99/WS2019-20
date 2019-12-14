import numpy as np
import math
from matplotlib import pyplot as plt
# n*d*logd(n)+(m+n)logd(n)

# m = n
x = np.arange(1,10,0.5)
n = 10
temp = np.log(n) / np.log(x)
y = temp * x * n + 2*n * temp

plt.title("m= Θ(n)")
plt.xlabel("x axis caption")
plt.ylabel("y axis caption, n = 10")
plt.plot(x, y)
plt.show()
