class Halde:
    class Henkel: # innere Klasse
        def __init__(self,x,pos):
            self.x = x
            self.pos = pos
    def __init__(self,maxLänge):
        self.maxLänge = maxLänge
        self.n = 0 # Länge der Halde
        self.a = [None]*(maxLänge+1)
         # Halde ist auf a[1] .. a[n] gespeichert. a[0] wird verschwendet
        self.h = [None]*(maxLänge+1)
         # zeigt auf die entsprechenden Henkel zurück:
         # Für i=1,...,n gilt:      h[i].pos == i
         # Für jeden Henkel H gilt: h[H.pos] == h
         
    def einfügen(self,x,s):
        if self.n>=self.maxLänge:
            raise RuntimeError("Feldüberlauf")
        self.n += 1
        self.h[self.n] = H = Halde.Henkel(x,self.n)
        self.a[self.n] = s
        self.zuklein(self.n)
        return H
    
    def entferneMin(self):
        if self.n<=0:
            raise RuntimeError("Halde ist leer")
        x = self.h[1].x
        self.n -= 1
        if self.n>0:
            self.vertausche(1,self.n+1)
            self.zugroß(1)
        return x
    
    def verkleinereSchlüssel(self,H,s):
        i = H.pos
        if s>self.a[i]:
            raise RuntimeError("Wert ist nicht kleiner.")
        self.a[i] = s
        self.zuklein(i)
    
    def istleer(self):
        return self.n==0
    
    ##### Hilfsfunktionen: ######
    def zuklein(self, i):
        # a[i] ist möglicherweise kleiner als sein Vorgänger.
        if i==1: return
        Vorgänger = i//2
        if self.a[i]<self.a[Vorgänger]:
            self.vertausche(i,Vorgänger)
            self.zuklein(Vorgänger)
    
    def zugroß(self, i):
        # a[i] ist möglicherweise größer als seine Nachfolger.
        if 2*i+1 <= self.n:
            if self.a[2*i]<self.a[2*i+1]: kleinsterNachfolger = 2*i
            else:                         kleinsterNachfolger = 2*i+1
        elif 2*i <= self.n:
            kleinsterNachfolger = 2*i
        else:
            return
        if self.a[i]>self.a[kleinsterNachfolger]:
            self.vertausche(i, kleinsterNachfolger)
            self.zugroß(kleinsterNachfolger)
    
    def vertausche(self, i1, i2):
        h1 = self.h[i1]
        h2 = self.h[i2]
        self.a[i1],self.a[i2] = self.a[i2],self.a[i1]
        self.h[i1],self.h[i2] = h2,h1
        h1.pos, h2.pos = i2,i1
    
