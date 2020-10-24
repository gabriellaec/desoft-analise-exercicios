def interseccao_valores(dic1,dic2):
    lista = []
    for v1 in dic1.values():
        for v2 in dic1.values():
            if v1 == v2:
                lista.append(v1)
                
    return lista