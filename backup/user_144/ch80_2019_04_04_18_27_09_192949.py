def interseccao_chaves(dic1,dic2):
    lista = []
    for k1 in dic1:
        for k2 in dic2:
            if k1 == k2:
                lista.append(k1)
                
    return lista
