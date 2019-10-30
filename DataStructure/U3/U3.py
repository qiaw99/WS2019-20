'''
import pysnooper
@pysnooper.snoop()
'''
__author__ = "Qianli and Nazar"
__copyright__ = "Copyright (c) 2019 qiaw99"
# https://github.com/qiaw99/WS2019-20/blob/master/LICENSE

# Task 18 a)
def verschiebe(F,b):
    ls = list(F)
    for i in range(0, len(ls), 2):
        ls[i] -= b
    return tuple(ls)

# Task 18 b): die ganze Graph wird nach links um 1 verschoben.

"""
H(x) = F(x) x < b
     = G(x) x >= b
"""
# Task 19
def fallunterscheidung(b, F, G):
    H = []
    if(F[0] >= b or G[-1] < b or F[-1] <= G[0]):
        return None
    # Find the right rand after b and store in i
    i = 0
    while(F[i] < b):
        i += 2

    # Fill H with F[x] to i
    for x in range(0, i):
        H.append(F[x])

    # Fill the b
    H.append(b)

    # Find the right rand(index) of G and store in j
    j = 0
    while(G[j] < b):
        j += 2

    # Fill the value
    H.append(G[j-1])

    ls = []
    for k in range(j, len(G)):
        ls.append(G[k])

    return tuple(H+ls)

def test():
		
	print()
	print("#######Aufgabe 18#######")
	F = eval(input("Bitte geben Sie die Funtion in Form Tupel:\n"))
	b = int(input("Um wie viel verschieben?\n"))
	if(b < 0):
		print("Verschieb nach rechts um " + str(b))
	elif(b > 0):
		print("Verschieb nach links um " + str(b))
	else:
		print("Bleibt unverändert")
	print("Das Ergebnis: ", verschiebe(F,b))

	print()
	print("#######Aufgabe 19#######")
	F = eval(input("Bitte geben Sie die erste Funtion in Form Tupel:\n"))
	G = eval(input("Bitte geben Sie die zweite Funtion in Form Tupel:\n"))
	b = int(input("Wie ist b?\n"))
	print("Das Ergebnis: ", fallunterscheidung(b,F,G))

def main():
	test()

if(__name__ == "__main__"):
	main()
