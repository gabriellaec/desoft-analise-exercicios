def interseccao_chaves (x, y):
    lista = []
    for i in x:
        if i in y:
            lista.append(i)
    return lista