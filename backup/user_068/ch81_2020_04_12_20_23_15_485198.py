def interseccao_valores(a, b):
    lista = []
    for i in a.values():
        if i in b.values():
            if i not in lista:
                lista.append(i)
    return lista
