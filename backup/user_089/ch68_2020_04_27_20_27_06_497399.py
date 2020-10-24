def separa_trios(x):
    i = 0
    lista = []
    while i < len(x):
        if x[i+2]:
            t = x[i:i+2]
            lista.append(t)
            i += 1
        if x[i+1]:
            d = x[i:i+1]
            lista.append(d)
            i = i +1
        else:
            s = x[i]
            lista.append(s)           
    return lista
