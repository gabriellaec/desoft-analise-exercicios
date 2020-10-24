def numero_no_indice(j):
    l = []
    for x in j:
        if j[x] == x:
            l.append(x)
    return l
