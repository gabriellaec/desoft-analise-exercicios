def encontra_maximo(m):
    i = 0
    k = 0
    while i < len(m)-1:
        t = 0
        while t < len(m[i])-1:
            if abs(m[i][t]) > k:
                k = abs(m[i][t])
            t += 1
        i += 1
    return k
                    