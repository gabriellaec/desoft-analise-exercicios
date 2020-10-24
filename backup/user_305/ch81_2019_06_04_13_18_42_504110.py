def interseccao_valores(dic1, dic2):
    lista = []
    for v in dic1.values():
        if v in dic2.values():
        	dic1[v].append(lista)
    for j in dic2.values():
        if j in dic1.values():
        	dic2[j].append(lista)
    return lista
    