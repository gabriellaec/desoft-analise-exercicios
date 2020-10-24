def interseccao_chaves(x,y):
    lista = []
    for i in x.keys():
        if i in y.keys():
            lista.append(i)
    return lista