#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

#string = sys.argv[1]

def initialize():
    string = "1 2 3, 1 -2, 2 -3"

    clauses = string.split(',')
    print("Boolean Formel: ", clauses)

    length = len(string)

    global ls, substitution, value
    value = []
    substitution = [0, 1]
    ls = [None] * length

    status = False
    counter = 0

    for k in clauses:
        for temp in k:
            if(temp == ' '):
                pass
            elif(temp == '-'):
                status = True
            else:
                if(status):
                    ls[counter] = -1 * int(temp)
                else:
                    ls[counter] = int(temp)
                counter += 1
                status = False
        ls[counter] = None
        counter += 1
    findElements()

# x is an integer
def substitute(x, value):
    global ls

    if value > 0:
        status = True
    else:
        status = False

    temp = []
    for e in ls:
        if(e == x):
            temp.append(e)

            # if 1 and x without negation, remove the whole clause
            if(status):
                removeAllNeighbors(ls.index(e))
            else:
                ls[ls.index(e)] = None
        elif(e == -1 * x):
            temp.append(e)

            # if 1 and x with negation, remove x
            if(status):
                ls[ls.index(e)] = None
            else:
                removeAllNeighbors(ls.index(e))
        else:
            pass

def removeAllNeighbors(index):
    global ls

    while(index <= len(ls) - 1 and ls[index] != None):
        ls[index] = None
        index += 1
    while(index >= 0 and ls[index] != None):
        ls[index] = None
        index -= 1

def isSatisfied():
    global ls
    temp = None
    counter = 0

    for x in ls:
        if(x == None):
            pass
        else:
            temp = x
            counter += 1

    if(counter == 1 or counter == 0):
        return True
    else:
        return False

def findElements():
    global ls, value
    for x in ls:
        if((x != None) and (x not in value) and ((-1 * x) not in value)):
            value.append(x)

def process():
    global value

    for x in range(1, max(value) + 1):
        for i in substitution:
            substitute(x, i)
            if(isSatisfied()):
                return True
    return False

def main():
    global ls, value

    initialize()
    if(process()):
        print("Bingo")
    else:
        print('Fuck')
    print(ls)

if __name__ == '__main__':
    main()
