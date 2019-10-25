import java.io.*;

class TopoSort {
    int n;
    Knoten[] Knotenliste; // Liste aller Knoten 1,...,n
    Knoten[] freieKnoten; // Menge Q der Knoten ohne Vorgänger
    int AnzfreieKnoten; // (als Stapel gespeichert)

    static IntReader input;

    public static void main(String[] args) throws IOException {
        input = new IntReader(args);
        TopoSort x = new TopoSort();
    }

    TopoSort() throws IOException {
        System.out.println("Topologischen Sortieren.");
        // Einlesen
        n = input.readInt();

        // Inititalisieren array:
        Knotenliste = new Knoten[n + 1];
        for (int i = 1; i <= n; i++) Knotenliste[i] = new Knoten(i);

        // Einlesen Kanten
        try {
            for (;;) {
                Knoten e = Knotenliste[input.readInt()];
                Knoten f = Knotenliste[input.readInt()];
                Kante x = new Kante(e, f);
                x.next = e.ersterNachfolger;
                e.ersterNachfolger = x;
                f.anzVorgänger++;
            }
        } catch (EOFException e) {}

        // Vorbereiten:
        freieKnoten = new Knoten[n];
        AnzfreieKnoten = 0;
        for (int i = 1; i <= n; i++) {
            Knoten e = Knotenliste[i];
            if (e.anzVorgänger == 0)
                freieKnoten[AnzfreieKnoten++] = e;
        }
        // Sortieren:
        System.out.println("\nFreie Knoten: ");
        sort:
            for (int i = 1; i <= n; i++) {
                if (AnzfreieKnoten == 0) {
                    int j = 1;
                    Knoten temp = Knotenliste[j];
                    while (temp.ersterNachfolger == null)
                        temp = Knotenliste[++j];
                    System.out.print("\n\nFehler. Die Eingabe enthält einen Kreis: " + temp);
                    Knoten loopElem = temp.ersterNachfolger.v;
                    while (!(loopElem.equals(temp))) {
                        System.out.print(" " + loopElem);
                        loopElem = loopElem.ersterNachfolger.v;
                    }
                    System.out.println(" ");
                    break sort;
                }
                // Wähle einen Knoten ohne Vorgänger
                Knoten x = freieKnoten[--AnzfreieKnoten];
                System.out.print(x + " ");
                // Entferne ausgehende Kanten:
                Kante z = x.ersterNachfolger;
                while (z != null) {
                    z.v.anzVorgänger--;
                    if (z.v.anzVorgänger == 0)
                        freieKnoten[AnzfreieKnoten++] = z.v;
                    z = z.next;
                }
            }
    }
}

class Knoten {
    int Name, anzVorgänger;
    Kante ersterNachfolger;
    Knoten(int i) {
        Name = i;
        anzVorgänger = 0;
        ersterNachfolger = null;
    }
    public String toString() {
        return String.valueOf(Name);
    }
}

class Kante {
    Knoten u, v;
    Kante next;
    Kante(Knoten uu, Knoten vv) {
        u = uu;
        v = vv;
    }
}
