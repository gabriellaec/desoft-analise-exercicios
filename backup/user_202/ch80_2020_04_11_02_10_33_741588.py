def interseccao_chaves(dic1,dic2):
    lista = []
    for k in dic1.keys():   
        for a in dic2.keys():
            if a == k:
                lista.append(k)
    return lista
    