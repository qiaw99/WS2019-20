import sys
import re
import random

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

checked_assignments = []

# +1 because leaving list[0] empty
length = find_max_len(clauses) + 1


values_list = [None] * (length)

def assign(variable):
    global values_list
    if variable > 0:
        values_list[variable] = True
    else:
        values_list[-variable] = False

def isSatisfied(formula):
    print("checking if satisfying ", formula)
    if (formula is None):
        return False
    if len(formula) == 0:
        return True
    temp = formula[0]
    for elem in formula:
        if temp != elem:
            return False
    return True

def simplify(variable, formula):
    global values_list
    negation = -1 * variable
    x = 0
    while x != len(formula):
        clause = formula[x]
        literals = re.findall(r'-?\d+', clause)
        #literals as integers
        res = list(map(int, literals))
        #if true
        if (variable in res):
            print("deleting ", clause)
            clauses.remove(clause)
        #if false
        elif (negation in res):
            #for replacing not last element
            print("removing ", negation, " from ", clause)
            if str(negation) + " " in clause:
                formula[x] = clause.replace(str(negation) + " ", "")
            elif str(negation) in clause:
                formula[x] = clause.replace(str(negation), "")
                print("The last element of the clause. It should be True. It is not. Error")
                return None
            else:
                print("dunno what to do with clause ", clause, " and negation: ", negation)
            if formula[x] == '':
                formula.remove(formula[x])
                x -= 1
            x += 1
        #not in clause
        else:
            x += 1
    print("formula after simplifying with ", variable, " : ", formula)
    print()
    return formula


def generate_assignment():
    global values_list, length, checked_assignments
    temp_list = [None] * (length)
    for i in range (1, length):
        temp_list[i] = random.choice([True, False])
    if temp_list in checked_assignments:
        print("generated: ", temp_list, " but it is in ", checked_assignments)
        generate_assignment()
    else:
        values_list = temp_list
        checked_assignments.append(temp_list)


def find_solution():
    global values_list, clauses, length, checked_assignments
    generate_assignment()
    formula_copy = clauses
    for i in range (1, length - 1):
        if (formula_copy is None):
            print('fucked up somewhere in simplifying, Trying once more')
            find_solution()
        if (values_list[i]):
            formula_copy = simplify(i, formula_copy)
        else:
            formula_copy = simplify(-i, formula_copy)
    if(isSatisfied(formula_copy)):
        if (len(formula_copy) != 0):
            if('-' in formula_copy[0]):
                values_list[-1] = False
            else:
                values_list[-1] = True
        print(values_list)
    else:
        if len(checked_assignments) == 2**(length - 1):
            print("all assignments checked. No solution")
            return
        else:
            print('fucked up, searching more')
            find_solution()



find_solution()

