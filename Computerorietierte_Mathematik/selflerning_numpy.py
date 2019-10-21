import numpy as np

g = list(range(10))

# sum of array
g_array = np.sum(g)
print(g_array)

# Constructor of array
a = np.array([1,2,3,4])
# a.shape = (4,)
b = np.array([10,11,12,13])
# a + b => array([11,13,15,17])
"""
In normal python: a + b -> [1,2,3,4,10,11,12,13]
"""

a.fill(1)
# a = [1,1,1,1]

##########################################################
# Control the type of array
b= np.array([1,2,3,4.0], dtype = int32)

c = np.array([[10,11,12],[20,21,22]])
"""
c.dtype dtype('int64')
c.ndim = 2
c.shape = (2,3)
"""
# Transport matrix
c.T = [[10,20],
        [11,21],
        [12,22]]
"""
c.size = 6
c.nbytes = 48
c[0,0] = 10  -> don't like in normal python c[0][0]
"""

##########################################################
# Slicing:  var[lower:upper:step]
a = np.array([10,11,12,13,14])
# a[::2] -> array([10,12,14])

a = [[0,1,2,3,4,5],
    [10,11,12,13,14,15],
    [20,21,22,23,24,25],
    [30,31,32,33,34,35],
    [40,41,42,43,44,45],
    [50,51,52,53,54,55]]

"""
a[0, 3:5] -> array([]3,4)
a[4:, 4:] -> array([44,45],[54,55])
a[:, 2]   -> array([2,12,22,32,42,52])
a[2::2, ::2]    -> array([20,22,24],[40,42,44])
"""

##########################################################
a = np.arange(25).reshape(5,5)
"""
array([[ 0,  1,  2,  3,  4],
    [ 5,  6,  7,  8,  9],
    [10, 11, 12, 13, 14],
    [15, 16, 17, 18, 19],
    [20, 21, 22, 23, 24]])
"""
red = a[:, ::2]
yellow = a[4]
blue = [1::2, 0:3:2]

##########################################################
a = np.array([3,-1,-2,4,-6,8])
"""
a < 0
-> array([False,  True,  True, False,  True, False])
a[a<0]  -> array([-1,-2,-6])
(a < 8).any()   -> true
(a , 8).all()   -> false

&(and) , |(or) , ~(not) , ^(xor)  -> bitwise operators
and or not -> binary operators

(a > 3) & (a < 8)   -> array([False,False,False,True,False,False])

a.nonzero(arr) -> get the array which is built with the numbers which are not equal 0
"""
