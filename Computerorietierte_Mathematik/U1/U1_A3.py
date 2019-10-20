'''
import pysnooper
@pysnooper.snoop()
'''
__author__ = "Qianli und Nazar"
__copyright__ = "Copyright (c) 2019 qiaw99"
# https://github.com/qiaw99/WS2019-20/blob/master/LICENSE

# Task a)
def ntobasetwo(n, c):
    # To guarantee that n and c are natural numbers <=> instance of Integer
    if(n >= 0 and isinstance(n, int) and isinstance(c, int)):
        if((n == 1 or n == 0) and c == 1):
            return str(n)
        elif((n == 1 or n == 0) and c != 1):
            return '0' * (c-1) + str(n)
        else:
            divider = n
            n = n >> 1
            if(divider / n == 2):
                temp = ntobasetwo(n, c - 1) + '0'
                if(len(temp) == c):
                    return temp
                elif(len(temp) > c):
                    raise Exception("The input length of c is not suitable!")
                else:
                    return '0' * (c - len(temp)) + temp
            else:
                temp = ntobasetwo(n, c - 1) + '1'
                if(len(temp) == c):
                    return temp
                elif(len(temp) > c):
                    raise Exception("The input length of c is not suitable!")                
                else:
                    return '1' * (c - len(temp)) + temp
    else:
        raise Exception("The input n is wrong!")

"""
Help function, to transform natural numbers into binary form.
@param n: a decimal numbers
"""
def dec2bin(n):     
    if(n==1 or n==0):
        return str(n)
    else:
        a = n
        n = n >> 1
        if(a / n == 2):
            return dec2bin(n) + '0'
        else:
            return dec2bin(n) + '1'

# The first element of the pair is value and the second is carry
def add(a, b):
    if(a == 1 and b == 1):
        return (0, 1)
    elif((a == 1 and b == 0) or (a ==0 and b == 1)):
        return (1, 0)
    else:
        return (0, 0)

# Task b)
# @param b: a binary String
def complement(b):
    # To guarantee that the string is builded with 0 and 1
    for i in range(len(b)):
        if(b[i] != '0' and b[i] != '1'):
            raise Exception("Please enter Strings which contain only '0' or '1'!")

    # One's complement
    length = len(b)
    temp = ''
    for i in range(length):
        if(b[i] == '1'):
            temp = temp + '0' 
        else:
            temp = temp + '1' 

    # Two's complement
    carry = 1
    str2 = ''
    for i in range(length - 1, -1, -1):
        pair = add(int(temp[i]), carry)
        value = pair[0]
        carry = pair[1]      
        str2 = str(value) + str2
    return str2

# @param b: a decimal number
def two_complement(b):
    if(isinstance(b, int)): 
        if(b < 0):
            b *= -1
            length = len(dec2bin(b))
            temp = ''
            str1 = dec2bin(b)
            return complement(str1)
        else:
            return dec2bin(b)
    else:
        raise Exception("The input b is not an Integer!")

# Task c)
def ztobasetwo(z, c):
    if(isinstance(z, int)):
        if(z < 0):
            temp = two_complement(z)
            if(len(temp) < c):
                return '1' * (c - len(temp)) + temp
            return two_complement(z)
        elif(z > 0):
            return ntobasetwo(z, c)
        else:
            return '0' * c
    else:
        raise Exception("The type of z is not Integer!")

def test():
    print()

    print("********** Aufgabe 3-a **********")
    print("Transformation from decimal number into binary number.")
    n = int(input("What's the number you would like to transform?\n"))
    c = int(input("And what about the length?\n"))
    print("The result is: " + ntobasetwo(n, c))

    print()
    print("********** Aufgabe 3-b **********")
    print("Transformation from decimal number into two's complement. Please don't enter ''.")
    b = input("What's the String you would like to transform?\n")
    print("The result is: " + complement(b))

    print()
    print("********** Aufgabe 3-c **********")
    z = int(input("What's the number you would like to transform?\n"))
    c = int(input("And what about the length?\n"))
    print("The result is: " + ztobasetwo(z, c))

def main():
    test()

if(__name__ == '__main__'):
    main()
