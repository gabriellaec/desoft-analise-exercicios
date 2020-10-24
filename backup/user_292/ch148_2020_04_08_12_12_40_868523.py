def conta_letras(l):
    D = {}
    p = []
    for i in range(len(l)):
        p.append(l[i])
    for i in p:
        if i not in D:
            D[i] = 1
        else:
            D[i] += 1
    return D