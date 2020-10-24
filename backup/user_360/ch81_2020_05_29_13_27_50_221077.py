def interseccao_valores(dic1, dic2):
    v1 = dic1.values()
    lista = []
    for i in v1:
        if i in dic2.values():
            lista.append(i)
            
    return lista