__author__ = "Qianli Wang und Nazar Sopiha"
__copyright__ = "Copyright (c) 2019 qiaw99"
# https://github.com/qiaw99/WS2019-20/blob/master/LICENSE

#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
    
print(private_quicksort([1,3,2,4,5]))
