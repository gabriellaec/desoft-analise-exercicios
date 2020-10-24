def interseccao_chaves(m,n):
    lista = []
    for k in m.keys():
        if k in n.keys():
            lista.append(k)
    return lista
    