def interseccao_chaves(dic1,dic2):
    lista1 = list(dic1.keys())
    lista2 = list(dic2.keys())
    lista = []
    for item in lista1:
        if item in lista2:
            lista.append(item)
    return lista