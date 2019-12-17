__author__ = "Qianli Wang und Nazar Sopiha"
__copyright__ = "Copyright (c) 2019 qiaw99"
# https://github.com/qiaw99/WS2019-20/blob/master/LICENSE

"""
Die Hauptidee ist, dass wir Bottom-Up dynammische Programmierung verwenden, 
damit wir viele unnötige Multiplikation einsparen können, dadurch die Laufzeit verkürzert wird.
"""

# (k - 1)- mal Multiplikationen
def fact(k):
    global ls
    ls = [-1 for i in range(k + 1)]
    
    if(k < 0):
        raise RuntimeError('k must be non-negative!')
    if k == 0: 
        ls[0] = 1
        return ls[0]
    elif(k == 1):
        ls[0] = 1
        ls[1] = 1
        return ls[1]
    else:
        ls[0] = 1
        ls[1] = 1
        for i in range(2, k):
            ls[i] = ls[i - 1] * i
        ls[k] = ls[k - 1] * k
        return ls[k]

# (k - 1)- mal Multiplikationen
def power(x, k):
    global temp
    temp = [-1 for i in range(k + 1)]
    
    if x == 0:
        raise RuntimeError("The base should not be 0!")
    if(k == 0):
        return 1
    else:
        temp[0] = 1
        temp[1] = x
        for i in range(2, k):
            temp[i] = temp[i - 1] * x
        temp[k] = temp[k - 1] * x
        return temp[k]

def func(x, k):
    global ls, temp
    # (2k - 2) mal Multiplikation
    power(x, k)
    fact(k)
    
    y = 1
    for i in range(k + 1):
        # k - mal Divisionen und k - mal Addition   -> insgesamt (4k - 2) -> in O(n)   
        y += temp[i] / ls[i]
    return y
       
def main():
    x = int(input("x?\n"))
    k = int(input("k?\n"))
    print("Das Ergebnis = ", func(x, k))
    
if __name__ == '__main__':
    main()

    
