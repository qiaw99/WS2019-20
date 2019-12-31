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

print(bubblesort([6,5,4,3,2,1]))        
print(hilfeArray_mergesort([6,3,10,5,2,9]))
