"""
f(j) := Länge k des längsten Präfixes b[0]...b[k-1] mit 0<=k<j,
        der ein Suffix von b[0]...b[j-1] ist.

      = max { k | 0<=k<j, b[:k] = b[j-k:j] }

für j=1,2,3,...,m
"""

def berechne_f(b):
    # Berechnung der Verschiebefunktion nach Definition
    # (in kubischer Zeit)
    m=len(b)
    return [None]+[max(k for k in range(j) if b[:k]==b[j-k:j])
                   for j in range(1,m+1)]

def berechne_f(b):
    # Berechnung der Verschiebefunktion in linearer Zeit
    m=len(b)
    f = [0]*(m+1)
    # f[1] = 0
    for j in range(1,m):
        # Berechne f[j+1]:
        k = f[j]
        while True:
            if b[k]==b[j]:
                f[j+1]=k+1
                break
            if k==0:
                f[j+1]=0
                break
            k=f[k] # verschieben
    return f

def berechne_f(b):
    # Berechnung der Verschiebefunktion in linearer Zeit
    m=len(b)
    f = [None,0] # f[1]=0
    k = 0
    for j in range(1,m):
        # Berechne f[j+1]:
        # k == f[j]
        while b[k]!=b[j] and k>0:
            k=f[k] # verschieben
        if b[k]==b[j]:
            k+=1
        f.append(k) # f[j+1]=k
    return f

def suche1(b,a): # erste Version aus der Vorlesung vom 21.11.2019
    "liefert erste Stelle, wo b in a vorkommt, oder None"
    m=len(b)
    n=len(a) # Annahme: m,n>0
    f = berechne_f(b)
    print(b,f)
    i=j=0
    while True:
        if b[j]==a[i]:
            i+=1
            j+=1
            if j==m:
                return i-m
            if i==n:
                return None
        else:
            if j==0:
                i+=1
                if i==n:
                    return None
            else:
                j=f[j]

def suche(b,a):
    return [suche1(b,a)]
                
def suche(b,a): # verbesserte Version
    m=len(b)
    n=len(a)
    f = berechne_f(b)
    print (b,f)
    i=j=0
    while True:
        if j==m:
            yield i-m
        if i==n:
            return
        if j<m and b[j]==a[i]:
            i+=1
            j+=1
        elif j==0:
            i+=1
        else:
            j=f[j]
    return
            
print(tuple(suche("ababa","abbabaabbaababba")))
print(tuple(suche("abab","abbabaabbaababba")))
print(tuple(suche("abba","abbabaabbaababba")))
print(tuple(suche("","abba")))
