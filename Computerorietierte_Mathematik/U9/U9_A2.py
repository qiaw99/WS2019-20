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
        #lists which store counters for each sort-algorithms
        helper1 = []
        helper2 = []

        maximum1 = []
        minimum1 = []
        durchschnitt1 = []
        
        maximum2 = []
        minimum2 = []
        durchschnitt2 = []
        for i in range(100):
            temp = [random.random() for j in range(10**k)]
            ls.append(temp)
            
            ######
            a, b = bubblesort(temp)
            helper1.append(b / 10**k)
            
            maximum1.append(max(helper1))
            minimum1.append(min(helper1))
            durchschnitt1.append(sum(helper1) / len(helper1))
            
            ######
            x, y = hilfeArray_mergesort(temp)
            helper2.append(y / 10**k)
            maximum2.append(max(helper2))
            minimum2.append(min(helper2))
            durchschnitt2.append(sum(helper2) / len(helper2))

        print("Waiting for the result... with length ", 10**k)
        print(len(maximum1))
        x1 = np.arange(0, 100)    
        y1 = np.array(maximum1)

        plt.title("Bubblesort")
        #plt.subplot(1, 1, 1)
        plt.plot(x1, y1, 'r', label = "maximum")
        
        y2 = np.array(minimum1)
        plt.plot(x1, y2, 'b', label = "minimum") 
        
        y3 = np.array(durchschnitt1)
        plt.plot(x1, y3, 'g', label = "durchschnitt") 
        plt.legend(loc = 'upper right')
        plt.show()
        
        x2 = np.arange(0, 100)    
        y4 = np.array(maximum2)

        plt.title("Mergsort")
        #plt.subplot(1, 1, 1)
        plt.plot(x2, y4, 'r', label = "maximum")
        
        y5 = np.array(minimum2)
        plt.plot(x1, y5, 'b', label = "minimum") 
        
        y6 = np.array(durchschnitt2)
        plt.plot(x1, y6, 'g', label = "durchschnitt") 
        plt.legend(loc = 'upper right')
        plt.show()

if __name__ == "__main__":
    main()


