def intergral(f):
    #((a,b),(c,d)) -> A function
    f = list(f)
    ls = []
    ls.append(f[0][0][0])
    
    for x in f:
        a = x[0][0]
        b = x[0][1]
        c = x[1][0]
        d = x[1][1]
        
        # Increasing of the linear
        k = (d - b) / float(c - a)
        ls.extend([k, c])
    
    return tuple(ls)

print(intergral((((1,2),(3,4)),((3,4),(7,8))))) 
