def gleichheit(F,G):
	if(len(F) != len(G)):
		return False
	for i in range (len(F)):
		if(F[i] != G[i]):
			return False
	return True

F = (1,2,3,4,5,6)
G1 = (1,2,3,4,5,6)
G2 = (1,2,3,4,5,5)

print(gleichheit(F,G1))
print(gleichheit(F,G2))
