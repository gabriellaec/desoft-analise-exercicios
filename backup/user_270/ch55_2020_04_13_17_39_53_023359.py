def encontra_maximo(m):
    i = 0
    k = 0
    while i < len(m)-1:
        t = 0
        while t < len(m[i])-1:
            if m[i][t] > k:
                k = m[i][t]
    return k
                    