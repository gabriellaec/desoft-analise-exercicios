def separa_trios(n):
    lista = []
    i = 1
    l = len(n)
    while i <= l:
        if l-(i-1) > 2:
            lista.append([n[i-1],n[i],n[i+1]])
            i = i + 3
        elif l - (i-1) == 2:
            lista.append([n[i-1],n[i]])
            i = i + 3
        else:
            lista.append([n[i-1]])
            i = i + 3
    return lista