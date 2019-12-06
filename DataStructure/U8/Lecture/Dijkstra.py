from Halde import Halde as PWSchlange

def dijkstra(s,V,E):
    d = {s: 0}
    f = {s: None}
    henkel = dict()
    U = PWSchlange(len(V)) # unfertige Knoten
    henkel[s] = U.einfügen(s,0)
    F = [] # fertige Knoten
    while not U.istleer():
        u = U.entferneMin()
        for v,c in E[u]: # c = c[u,v]
            if v not in d:
                d[v] = d[u]+c
                f[v] = u
                henkel[v] = U.einfügen(v,d[v])
            else:
                if d[u]+c<d[v]:
                    d[v] = d[u]+c
                    f[v] = u
                    U.verkleinereSchlüssel(henkel[v],d[v])
    for u in d:
        print("Knoten {}: Distanz ={:3}, Vorgänger = {}, kürzester Weg = {}".format
              (u,d[u],f[u], bestimme_Weg(u,f)))

def bestimme_Weg(u,f):
    W = [u]
    while f[u] is not None:
        u=f[u]
        W.append(u)
    W.reverse()
    return W

if __name__=="__main__":
    E = {
        "a": [("b",5),("c",2)],
        "b": [("c",4),("d",8)],
        "c": [("b",1),("e",9)],
        "d": [("f",11),("e",9)],
        "e": [("f",2),("t",6)],
        "f": [("a",9),("t",5)],
        "t": [] }
    V = list(E)
    dijkstra("a",V,E)
        
