__author__ = "Qianli and Nazar"

# Task 18 a)
def verschiebe(F,b):
	ls = list(F)
	for i in range(0, len(ls), 2):
		ls[i] -= b
	return tuple(ls)
# Task 18 b): die ganze Graph wird nach links um 1 verschoben.

F = (0,1,1,2,2,3,3,4,4)
# print(verschiebe(F,1))

"""
H(x) = F(x) x < b
	 = G(x) x >= b
"""
# Task 19
def fallunterscheidung(b, F, G):
	H = []
	if(F[0] >= b or G[len(G)-1] < b):
		return None
	# Find the left rand before b and store in temp1
	i = 0
	while(F[i] < b):
		i += 2
	temp1 = i - 2

	# Fill H with F[i] to temp1
	for x in range(0, temp1 + 2):
		H.append(F[x])

	# Fill the b
	H.append(b)

	# Find the right rand(index) of G and store in temp2
	j = 0
	while(G[j] < b):
		j += 2
	temp2 = j - 2

	# Fill the value 
	H.append(G[temp2+1])

	ls = []
	for k in range(temp2+2, len(G)):
		ls.append(G[k])

	return tuple(H+ls)

F = (0,3,2)
G = (-1,4,5)
print(fallunterscheidung(1,F,G))
