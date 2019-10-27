

def berechne(F,x):
    if x<F[0] or x>=F[-1]: return None
    i=2
    while x>=F[i]: i+=2
    return F[i-1]

def add(F,G):
    ff = fg = fh = None
    i = j = 0
    ausgabe = (max(F[0],G[0]),)
    while True:
        # Invariante:
        # ff ist der Wert der Funktion F links von F[i]
        # fg ist der Wert der Funktion G links von G[j]
        # fh=ff+fg
        if F[i]<G[j]:
            if fh != None: ausgabe += (fh,F[i])
            if i==len(F)-1: return ausgabe
            ff=F[i+1]
            i+=2
        elif F[i]>G[j]:
            if fh != None: ausgabe += (fh,G[j])
            if j==len(G)-1: return ausgabe
            fg=G[j+1]
            j+=2
        else: # F[i]==G[j]:
            if fh != None: ausgabe += (fh,G[j])
            if i==len(F)-1 or j==len(G)-1: return ausgabe
            ff=F[i+1]
            fg=G[j+1]
            i+=2
            j+=2
        if fg!=None and ff!=None: fh=ff+fg

                 
F1 = (0,2,3,1,5,5,10)
G1 = (1,-4,3,8,11)
H1 = add(F1,G1)

print("2F ",add(F1,F1))
print(" F ",F1)
print(" G ",G1)
print("F+G",H1)

print("\n     x  F(x)  G(x) F(x)+G(x)")
for i in range(-2,13):
    x = i + 0.5
    print ((" %5s"*4)%(x,berechne(F1,x),berechne(G1,x),berechne(H1,x)))
      
