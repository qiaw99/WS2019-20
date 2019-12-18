#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np

def ggT_tumb(a, b):
    ggt = 1
    counter = 0
    temp = a if a <= b else b
    for i in range(2, temp + 1):
        counter += 2
        if (a % i) == 0 and (b % i )== 0:
            ggt = i
    return (ggt, counter)

def ggT_tumbpp(a, b):
    temp = a if a <= b else b
    counter = 0
    for i in range(temp, 1, -1):
        counter += 2
        if((a % i == 0) and (b % i == 0)):
            return (i, counter)
    return (1, counter)

def ggT_euclid(a, b):
    m = a if a >= b else b
    n = b if a >= b else a
    counter = 0
    while(n > 0):
        r = m % n
        counter += 1
        m = n
        n = r
    return (m, counter)

def main():
    # {100,...,1000}
    a = np.random.randint(900, size = 1000) + 100
    b = np.random.randint(900, size = 1000) + 100
    ls = []
    counter = 0
    for i in range(1000):
        counter = ggT_tumb(a[i], b[i])[1]
        ls.append(counter)

    print(ls)

if __name__ == "__main__":
    main()
