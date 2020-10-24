def encontra_maximo(m):
    l1 = []
    i = 0
    while i<len(m):
        l1.append(abs(m[i][0]))
        l1.append(abs(m[i][1]))
        l1.append(abs(m[i][2]))
        i+=1
    x = max(l1)
    return x
                 
    