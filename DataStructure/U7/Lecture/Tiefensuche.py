besucht = {}
f = {} # Vorgängerzeiger
TNummer = {}

def initialisiere():
    global num,besucht,d
    num = 0
    for u in V: # alle Knoten
        besucht[u] = False
        f[u] = None

def T(u): # rekursive Prozedur für die Tiefensuche
    global num
    num += 1
    TNummer[u] = num
    besucht[u] = True
    for v in E[u]: # alle Kanten (u,v), die von u ausgehen
        if not besucht[v]:
            f[v] = u
            T(v)

def Tiefensuche():
    initialisiere()
    for u in V:
        if not besucht[u]:
            T(u)

### Testdaten:
            
V = "abcdef"
E = {"a":"bd", "b": "a", "c": "f", "d": "ba", "e": "f", "f":"cab"}

Tiefensuche()
print (f)
print (TNummer)

    
