def simplifica_dict(x):
    lista = []
    for e in x:
        if e not in lista:
            lista.append(e)
        if x[e] not in lista:
            lista.append(x[e])
    return lista