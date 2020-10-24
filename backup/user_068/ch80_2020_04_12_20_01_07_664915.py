def interseccao_chaves(a, b):
    lista = []
    for i in a.keys():
        if i in b.keys():
            if i not in lista:
                lista.append(i)
    return lista
