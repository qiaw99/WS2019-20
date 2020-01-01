__author__ = "Qianli Wang und Nazar Sopiha"
__copyright__ = "Copyright (c) 2019 qiaw99"
# https://github.com/qiaw99/WS2019-20/blob/master/LICENSE

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt

# Aufgabe a)
def bubblesort(ls):
    temp = 0
    swap = True
    stop = len(ls) - 1
    while swap:
        swap = False
        for i in range(stop):
            if(ls[i] > ls[i + 1]):
                temp += 1
                ls[i], ls[i + 1] = ls[i + 1], ls[i]
                swap = True
        stop = stop - 1
    return (ls, temp)

# Aufgabe b)    
#implementiert mithilfe einer Hilfeliste, damit wir auf die Rekursion verzichten können
def hilfeArray_mergesort(A):    
    N = len(A)
    partsLength = 1
    while partsLength < N:
        for i in range(0, N // partsLength, 2):
            hilfeArray_merge(A, i * partsLength, (i + 1) * partsLength)
        partsLength <<= 1 
    return (A, counter)

def hilfeArray_merge(A, firstPartlowerIndex, secondPartlowerIndex):
    global counter 
    counter = 0
    firstPartIndex = firstPartlowerIndex
    secondPartIndex = secondPartlowerIndex
    rightBoundary = min(2 * secondPartlowerIndex - firstPartlowerIndex - 1, len(A) - 1)
    mergedList = []
    
    while secondPartlowerIndex - 1 - firstPartIndex >= 0 and rightBoundary - secondPartIndex >= 0:
        counter += 2
        if A[firstPartIndex] <= A[secondPartIndex]:
            counter += 1
            mergedList.append(A[firstPartIndex])
            firstPartIndex += 1
        else:
            counter += 1
            mergedList.append(A[secondPartIndex])
            secondPartIndex += 1
            
    while secondPartlowerIndex - 1 - firstPartIndex >= 0:
        counter += 1
        mergedList.append(A[firstPartIndex])
        firstPartIndex += 1
        
    while rightBoundary - secondPartIndex >= 0:
        counter += 1
        mergedList.append(A[secondPartIndex])
        secondPartIndex += 1
        
    for i in range(firstPartlowerIndex, rightBoundary + 1):
        A[i] = mergedList[i - firstPartlowerIndex]          

def main():
    for k in range(1, 5):
        ls = []
        for i in range(100):
            temp = [random.random() for j in range(10**k)]
            ls.append(temp)
            
        #lists which store counters for each sort-algorithms
        helper1 = []
        helper2 = []

        print("Waiting for the result... with length ", 10**k)
        
        maximum = []
        minimum = []
        durchschnitt = []
        for x in ls:
            # a is sorted lists and b is counter
            a, b = bubblesort(x)
            helper1.append(b)
            
            maximum.append(max(helper1))
            minimum.append(min(helper1))
            durchschnitt.append(sum(helper1) / len(helper1))
            
            a, b = hilfeArray_mergesort(x)
            helper2.append(b)
        
        
        x = np.arange(0, 100)    
        y1 = np.array(maximum)

        plt.subplot(1, 1, 1)
        plt.plot(x, y1, color = 'r', label = "maximum")
        
        y2 = np.array(minimum)
        plt.plot(x, y2, 'b', label = "minimum") 
        
        y3 = np.array(durchschnitt)
        plt.plot(x, y2, 'g', label = "durchschnitt") 
        plt.show()
        
        """
        print("Die Länge ist: ", 10**k)
        print("******Bubblesort******")
        print("Der größte Aufwand: ", max(helper1))
        print("Der kleinste Aufwand: ", min(helper1))
        print("Der durchschnittliche Aufwand: ", sum(helper1) / len(helper1))
        print()
        print("******Mergesort******")
        print("Der größte Aufwand: ", max(helper2))
        print("Der kleinste Aufwand: ", min(helper2))
        print("Der durchschnittliche Aufwand: ", sum(helper2) / len(helper2))
        """
if __name__ == "__main__":
    main()



