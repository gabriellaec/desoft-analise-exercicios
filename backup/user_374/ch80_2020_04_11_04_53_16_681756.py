def  interseccao_chaves(d1,d2):
    k1 = d1.keys()
    lista = []
    for i in k1:
        if i in d2.keys():
            lista.append(i)
            
    return lista
