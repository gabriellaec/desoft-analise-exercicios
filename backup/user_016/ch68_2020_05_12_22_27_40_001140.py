def separa_trios(x):
    lista = []
    i = -3
    u = 0
    while u <= len(x):
        i += 3
        u += 3
        if len(x[i:u]) == 3:
            lista.append(x[i:u])
        elif len(x[i:]) != 0:
            lista.append(x[i:])
    return lista