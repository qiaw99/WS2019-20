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
            x.next = e.ersterNachfolger
            e.ersterNachfolger = x
            f.anzVorgänger += 1
    except StopIteration:
        pass
        
    # Vorbereiten:
    freieKnoten = [None]*n
    # explizit programmierter Stapel;
    # könnte auch mit append() (=push) und pop() geschrieben werden.    
    AnzfreieKnoten = 0;
    for i in range(1,n+1):
        e = Knotenliste[i]
        if e.anzVorgänger==0:
            freieKnoten[AnzfreieKnoten]=e
            AnzfreieKnoten += 1

    # Sortieren:
    print("");
    for i in range(1,n+1):
        if AnzfreieKnoten == 0:
            print("Die Eingabe enthält einen Kreis.")
            return
        # Wähle einen Knoten ohne Vorgänger
        AnzfreieKnoten -= 1
        x = freieKnoten[AnzfreieKnoten]
        print(x)
        # Entferne ausgehende Kanten:
        z = x.ersterNachfolger
        while z != None:
            z.v.anzVorgänger -= 1
            if z.v.anzVorgänger == 0:
                freieKnoten[AnzfreieKnoten]=z.v
                AnzfreieKnoten += 1
            z = z.next

class Knoten:
    def __init__(self, i):
        self.Name = i
        self.anzVorgänger = 0
        self.ersterNachfolger = None
    def __str__(self):
        return str(self.Name)

class Kante:
    def __init__(self, u, v):
        self.u = u
        self.v = v

TopoSort()        
