import java.io.*;

public class TopoSort {
    int n;
    Knoten[] Knotenliste; // Liste aller Knoten 1,...,n
    Knoten[] freieKnoten; // Menge Q der Knoten ohne Vorgänger
    int AnzfreieKnoten; // (als Stapel gespeichert)

    static IntReader input;

    public static void main(String[] args) throws IOException {
        input = new IntReader(args);
        TopoSort x = new TopoSort();
    }

    public TopoSort() throws IOException {
        System.out.println("Topologischen Sortieren.");
        // Einlesen
        n = input.readInt();

        // Inititalisieren array:
        Knotenliste = new Knoten[n + 1];
        for (int i = 0; i < n; i++) Knotenliste[i] = new Knoten(i);

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
        for (int i = 0; i < n; i++) {
            Knoten e = Knotenliste[i];
            if (e.anzVorgänger == 0)
                freieKnoten[AnzfreieKnoten++] = e;
        }
        // Sortieren:
        System.out.println("");
        sort:
            for (int i = 1; i <= n; i++) {
                if (AnzfreieKnoten == 0) {
                    // after this instruction will be "break" executed,
                    // so it has no influence on running time of for-loop
                    Knoten temp = Knotenliste[0];
                    while (temp.anzVorgänger == 0) {
                          temp = temp.ersterNachfolger.v;
                    }
                    Knoten inLoop = temp;
                    System.out.println("Loop is: " + temp);
                    while ((inLoop.ersterNachfolger).equals(temp) == false) {
                        System.out.println(inLoop + " ");
                        inLoop = inLoop.ersterNachfolger.v;
                    }
                    break sort;
                }
                // Wähle einen Knoten ohne Vorgänger
                Knoten x = freieKnoten[--AnzfreieKnoten];
                System.out.println(x);
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
    
    public Knoten(int i) {
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
    
    public Kante(Knoten uu, Knoten vv) {
        u = uu;
        v = vv;
    }
}
