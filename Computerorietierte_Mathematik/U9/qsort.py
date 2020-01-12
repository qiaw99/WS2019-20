__author__ = "Qianli Wang und Nazar Sopiha"
__copyright__ = "Copyright (c) 2019 qiaw99"
# https://github.com/qiaw99/WS2019-20/blob/master/LICENSE

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random
import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 3
def quicksort(A, low, high):
    global counter 
    if low < high:
        counter += 1
        m = partition(A, low, high)
        quicksort(A, low, m - 1)
        quicksort(A, m + 1, high)
    return A
        
def partition(A, low, high):
    global counter 
    pivot = A[low]
    i = low
    for j in range(low + 1, high + 1):
        if A[j] < pivot:
            counter += 1
            i = i + 1
            A[i], A[j] = A[j], A[i]
    A[i], A[low] = A[low], A[i]
    return i

def private_quicksort(A):
    global counter 
    counter = 0
    
    return (quicksort(A, 0, len(A) - 1), counter)
    
def main():
    for k in range(1, 5):
        ls = []
        #lists which store counters for each sort-algorithms
        helper1 = []

        maximum1 = []
        minimum1 = []
        durchschnitt1 = []
        for i in range(100):
            temp = [random.random() for j in range(10**k)]
            ls.append(temp)
            
            ######
            a, b = private_quicksort(temp)
            helper1.append(b / 10**k)
            
            maximum1.append(max(helper1))
            minimum1.append(min(helper1))
            durchschnitt1.append(sum(helper1) / len(helper1))
           

        print("Waiting for the result... with length ", 10**k)
        print(len(maximum1))
        x1 = np.arange(0, 100)    
        y1 = np.array(maximum1)

        plt.title("Quicksort")
        #plt.subplot(1, 1, 1)
        plt.plot(x1, y1, 'r', label = "maximum")
        
        y2 = np.array(minimum1)
        plt.plot(x1, y2, 'b', label = "minimum") 
        
        y3 = np.array(durchschnitt1)
        plt.plot(x1, y3, 'g', label = "durchschnitt") 
        plt.legend(loc = 'upper right')
        plt.show()

if __name__ == '__main__':
    main()
