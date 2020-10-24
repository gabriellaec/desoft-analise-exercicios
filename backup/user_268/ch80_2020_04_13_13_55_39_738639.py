def interseccao_chaves(d1, d2):
    c1 = d1.keys()
    c2 = d2.keys()
    lista = []
    for i in c1:
        if i in c2 and i not in lista:

            lista.append(i)
    return lista
        