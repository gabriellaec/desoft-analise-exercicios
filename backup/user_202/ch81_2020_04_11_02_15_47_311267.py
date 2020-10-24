def interseccao_valores(dic1,dic2):
    lista = []
    for k in dic1.values():   
        for a in dic2.values():
            if a == k:
                lista.append(k)
    return lista
        