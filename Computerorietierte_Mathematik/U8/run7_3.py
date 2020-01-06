#!/usr/bin/env python
# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np

def ggT_tumb(a, b):
    ggt = 1
    counter = 1
    temp = a if a <= b else b
    for i in range(2, temp + 1):
        counter += 2
        if (a % i) == 0 and (b % i )== 0:
            ggt = i
    return (ggt, counter)

def ggT_tumbpp(a, b):
    temp = a if a <= b else b
    counter = 1
    for i in range(temp, 1, -1):
        counter += 2
        if((a % i == 0) and (b % i == 0)):
            return (i, counter)
    return (1, counter)

def ggT_euclid(a, b):
    m = a if a >= b else b
    n = b if a >= b else a
    counter = 2
    while(n > 0):
        r = m % n
        counter += 1
        m = n
        n = r
    return (m, counter)

def draw_graph_ggT_tumb():
    # {100,...,1000}
    a = np.random.randint(900, size = 1000) + 100
    b = np.random.randint(900, size = 1000) + 100

    ls = []
    for i in range(1000):
        counter = ggT_tumb(a[i], b[i])[1]
        ls.append(counter)

    gr1 = 0
    gr2 = 0
    gr3 = 0
    gr4 = 0
    gr5 = 0
    gr6 = 0
    gr7 = 0
    gr8 = 0
    gr9 = 0
    gr10 = 0
    maximum = max(ls)
    minimum = min(ls)

    for x in ls:
        if x < maximum/10:
            gr1 += 1
        elif x < 2*maximum/10:
            gr2 += 1
        elif x < 3*maximum/10:
            gr3 += 1
        elif x < 4*maximum/10:
            gr4 += 1
        elif x < 5*maximum/10:
            gr5 += 1
        elif x < 6*maximum/10:
            gr6 += 1
        elif x < 7*maximum/10:
            gr7 += 1
        elif x < 8*maximum/10:
            gr8 += 1
        elif x < 9*maximum/10:
            gr9 += 1
        else:
            gr10 += 1

    y = [gr1, gr2, gr3, gr4, gr5,gr6, gr7, gr8, gr9, gr10]
    x = ['>' + str(i) for i in range (0, maximum + 1, 200)]

    plt.title("ggT_tumb; max is " + str(maximum) + " min is " + str(minimum))
    plt.xlabel("Gruppe nach der Anzahl der Vergleiche")
    plt.ylabel("Anzahl der Elemente in der Gruppe")
    plt.bar(range(len(y)), y, fc = 'r', tick_label = x)
    plt.savefig("histtumb.png")
    plt.show()

def draw_graph_ggT_tumbpp():
    # {100,...,1000}
    a = np.random.randint(900, size = 1000) + 100
    b = np.random.randint(900, size = 1000) + 100

    ls = []
    for i in range(1000):
        counter = ggT_tumbpp(a[i], b[i])[1]
        ls.append(counter)

    gr1 = 0
    gr2 = 0
    gr3 = 0
    gr4 = 0
    gr5 = 0
    gr6 = 0
    gr7 = 0
    gr8 = 0
    gr9 = 0
    gr10 = 0
    maximum = max(ls)
    minimum = min(ls)

    for x in ls:
        if x < maximum/10:
            gr1 += 1
        elif x < 2*maximum/10:
            gr2 += 1
        elif x < 3*maximum/10:
            gr3 += 1
        elif x < 4*maximum/10:
            gr4 += 1
        elif x < 5*maximum/10:
            gr5 += 1
        elif x < 6*maximum/10:
            gr6 += 1
        elif x < 7*maximum/10:
            gr7 += 1
        elif x < 8*maximum/10:
            gr8 += 1
        elif x < 9*maximum/10:
            gr9 += 1
        else:
            gr10 += 1

    y = [gr1, gr2, gr3, gr4, gr5,gr6, gr7, gr8, gr9, gr10]
    x = ['>' + str(i) for i in range (0, maximum + 1, 200)]

    plt.title("ggT_tumbpp; max is " + str(maximum) + " min is " + str(minimum))
    plt.xlabel("Gruppe nach der Anzahl der Vergleiche")
    plt.ylabel("Anzahl der Elemente in der Gruppe")
    plt.bar(range(len(y)), y, fc = 'r', tick_label = x)
    plt.savefig("histtumbpp.png")
    plt.show()

def draw_graph_ggT_euclid():
    # {100,...,1000}
    a = np.random.randint(900, size = 1000) + 100
    b = np.random.randint(900, size = 1000) + 100

    ls = []
    for i in range(1000):
        counter = ggT_euclid(a[i], b[i])[1]
        ls.append(counter)

    gr1 = 0
    gr2 = 0
    gr3 = 0
    gr4 = 0
    gr5 = 0
    gr6 = 0
    gr7 = 0
    gr8 = 0
    gr9 = 0
    gr10 = 0
    maximum = max(ls)
    minimum = min(ls)

    for x in ls:
        if x < maximum/10:
            gr1 += 1
        elif x < 2*maximum/10:
            gr2 += 1
        elif x < 3*maximum/10:
            gr3 += 1
        elif x < 4*maximum/10:
            gr4 += 1
        elif x < 5*maximum/10:
            gr5 += 1
        elif x < 6*maximum/10:
            gr6 += 1
        elif x < 7*maximum/10:
            gr7 += 1
        elif x < 8*maximum/10:
            gr8 += 1
        elif x < 9*maximum/10:
            gr9 += 1
        else:
            gr10 += 1

    y = [gr1, gr2, gr3, gr4, gr5,gr6, gr7, gr8, gr9, gr10]
    x = ['>' + str(i) for i in range (0, 10)]

    plt.title("ggT_euclid; max is " + str(maximum) + " min is " + str(minimum))
    plt.xlabel("Gruppe nach der Anzahl der Vergleiche")
    plt.ylabel("Anzahl der Elemente in der Gruppe")
    plt.bar(range(len(y)), y, fc = 'r', tick_label = x)
    plt.savefig("histeuclid.png")
    plt.show()

def main():
    draw_graph_ggT_tumb()
    draw_graph_ggT_tumbpp()
    draw_graph_ggT_euclid()

if __name__ == "__main__":
    main()
