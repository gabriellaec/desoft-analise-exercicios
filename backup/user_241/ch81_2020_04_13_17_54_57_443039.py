def interseccao_valores(x,y):
    lista = []
    for i in x.values():
        if i in y.values():
            lista.append(i)
    return lista