import math

f1 = lambda x : x * (x + 2)
f2 = lambda x : math.sqrt(x + 1) - 1

def concat(f1,f2):
	return lambda x : f1(f2(x))

g = concat(f1,f2)
h = concat(f2,f1)
t = 13
"""
for i in range(13):
	print("f1(t) ",f1(-1+10**i))
	print("f2(t) ",f2(-1+10**i),"\n")
"""
#print("f1(f2(t)): ", f1(f2(t)))
#print("f2(f1(t)): ", f2(f1(t)))
print("g(t): ",g(t))	
print("h(t): ",h(t))
