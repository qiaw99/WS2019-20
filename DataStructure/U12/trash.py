import sys
import re

def find_max_len(clauses):
    max = 0
    for clause in clauses:
        if len(clause) > max:
            max = len(clause)
    return max

input = "1 2 -3, -1 3, -2"

clauses = input.split(", ")

n = find_max_len(clauses)

values_list = [None] * n

def assign(variable, value):
    global values_list
    values_list[variable] = value

def simplify(variable, value):
    global clauses
    negation = -1 * variable
    if value == True:
        x = 0
        while x != len(clauses):
            clause = clauses[x]
            literals = re.findall(r'-?\d+', clause)
            res = list(map(int, literals))
            if (variable in res):
                clauses.remove(clause)
            elif (negation in res):
                print("clause , variable", clause, " ", negation)
                clause = clause.replace(str(negation), "")
                x += 1
            else:
                x += 1
        print(clauses)

simplify(1, True)

