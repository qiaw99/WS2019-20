import sys
import re

#we assume that all indexes 1...n are there

def find_max_len(clauses):
    max = 0
    for clause in clauses:
        length = len(clause.split(" "))
        if length  > max:
            max = length
    return max

input = "1 2 -3, -1 3, -2"

clauses = input.split(", ")

length = find_max_len(clauses)

# +1 because leaving list[0] empty
values_list = [None] * (length + 1)

def assign(variable):
    global values_list
    if variable > 0:
        values_list[variable] = True
    else:
        values_list[-variable] = False

def isSatisfied():
    global clauses
    if len(clauses) == 0:
        return True
    temp = clauses[0]
    for elem in clauses:
        if temp != elem:
            return False
    return True

def simplify(variable):
    global clauses
    negation = -1 * variable
    x = 0
    while x != len(clauses):
        clause = clauses[x]
        literals = re.findall(r'-?\d+', clause)
        #literals as integers
        res = list(map(int, literals))
        #if true
        if (variable in res):
            clauses.remove(clause)
        #if false
        elif (negation in res):
            #for replacing not last element
            if str(negation) + " " in clause:
                clauses[x] = clause.replace(str(negation) + " ", "")
            else:
                clauses[x] = clause.replace(str(negation), "")
            if clauses[x] == '':
                clauses.remove(clauses[x])
                x -= 1
            x += 1
        #not in clause
        else:
            x += 1
    if isSatisfied():
        print('sol found')
        return

    print(clauses)

assign(1)
simplify(1)
print(values_list[1:])

