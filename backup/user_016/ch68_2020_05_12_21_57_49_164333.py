def separa_trios(x):
    lista = []
    i = 0
    u = 3
    while u <= len(x):
        lista.append(x[i:u])
        i += 3
        u += 3
    return lista