import pysnooper
@pysnooper.snoop()

def ntobasetwo(n, c):
    if(n == 1 or n == 0):
        return str(n)
    else:
        divider = n
        n = n>>1
        if(divider / n == 2):
            temp = ntobasetwo(n, c-1) + '0'
            if(len(temp) == c):
                return temp
            elif(len(temp) > c):
                raise Exception("The input length of c is not suitable!")
            else:
                return '0' * (c - len(temp)) + temp
        else:
            temp = ntobasetwo(n, c-1) + '1'
            if(len(temp) == c):
                return temp
            elif(len(temp) > c):
                raise Exception("The input length of c is not suitable!")                
            else:
                return '1' * (c - len(temp)) + temp

def dec2bin(n):     
    if(n==1 or n==0):
        return str(n)
    else:
        a = n
        n = n>>1
        if(a/n == 2):
            return dec2bin(n) + '0'
        else:
            return dec2bin(n) + '1'

def complement(b):
    length = len(dec2bin(b))
    for i in range(length):
        str1 = str(b)
        if(str1[i] == '1'):
            str1.replace('1', '0')
        else:
            str1.replace('0', '1')
    return str1

print(complement(12))
str = "12345"
print(str[1])
