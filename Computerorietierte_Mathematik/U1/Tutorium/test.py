import numpy as np

ls = []
for i in range(1,100,2):
    ls.append(i)

for i in range(len(ls)):
    ls[i] *= 3

"""
ls = np.array(ls) * 3 
"""

print(ls[26])
print(np.array(ls)*3)
