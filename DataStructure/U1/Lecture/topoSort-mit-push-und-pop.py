import intReader

def TopoSort():
    print ("Topologischen Sortieren.")
    # Einlesen
    input = intReader.readInt()
    n = next(input)

    # Inititalisieren array:
    Knotenliste = [None] + [ Knoten(i) for i in range(1,n+1) ]
    
    # Einlesen Kanten
    try:
        while True:
            e = Knotenliste[next(input)]
            f = Knotenliste[next(input)]
            x = Kante(e,f)
            e.Nachfolgerliste.append(x)
            f.anzVorgänger+=1
    except StopIteration:
        pass
        
    # Vorbereiten:
    freieKnoten = []
    for i in range(1,n+1):
        e = Knotenliste[i]
        if e.anzVorgänger==0:
            freieKnoten.append(e)

    # Sortieren:
    print("");
    for i in range(1,n+1):
        if freieKnoten == []:
            print("Die Eingabe enthält einen Kreis.")
            return
        # Wähle einen Knoten ohne Vorgänger
        x = freieKnoten.pop()
        print(x)
        # Entferne ausgehende Kanten:
        for z in x.Nachfolgerliste:
            z.v.anzVorgänger -= 1
            if z.v.anzVorgänger == 0:
                freieKnoten.append(z.v)

class Knoten:
    def __init__(self, i):
        self.Name = i
        self.anzVorgänger = 0
        self.Nachfolgerliste = []
    def __str__(self):
        return str(self.Name)

class Kante:
    def __init__(self, u, v):
        self.u = u
        self.v = v

TopoSort()        
