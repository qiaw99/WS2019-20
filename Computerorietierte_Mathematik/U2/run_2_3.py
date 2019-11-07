__author__ = "Qianli und Nazar"
__copyright__ = "Copyright (c) 2019 qiaw99"
# https://github.com/qiaw99/WS2019-20/blob/master/LICENSE

from plotErrors import *
from U2_A3 import *

# Aufgabe 3d)
def fill_src_arr (X):
    for i in range (1 ,100001):   #first value is 0.001, goes till (upper bound - 1)
        X.append(i/1000)
    return X
    
def fill_abs_arr(src, abs_err):
    for i in range (100000):
        rounded_num = fixedpoint(src[i])
        abs_error = absoluteError(src[i], rounded_num)
        abs_err.append(abs_error)
    return abs_err
    
def fill_rel_arr(src, abs_err, rel_err):
    for i in range (100000):
        rel_error = relativeError(src[i], abs_err[i])
        rel_err.append(rel_error)
    return rel_err
    
def print_err():
    src = []     #source array
    abs_err = [] # array of absoulte errors
    rel_err = [] # array of relative errors
    fill_src_arr(src)
    fill_abs_arr(src, abs_err)
    fill_rel_arr(src, abs_err, rel_err)
    plotErrors(src, abs_err, rel_err)
    print("Die Bilder werden schon hergestellt.")
   
def main(): 
	print_err()

if(__name__ == '__main__'):
	main()
