def hashfunction():
    t_values = [0, 1, 2, 3, 4, 5, 13, 20]
    res = {}
    for t in t_values:
        temp = [0 for i in range(1024)]
        for i in range(1024):
            temp[ (t*i) % 1024] += 1
        m = max(temp)
        print(m)
        res[t] = m
    print(res)
    return res

hashfunction()
print("Permutation für t = 1, 3, 5, 13")
