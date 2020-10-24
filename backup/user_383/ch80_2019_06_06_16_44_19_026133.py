def interseccao_chaves(dic1,dic2):
    lista_vazia=[]
    for k1 in dic1.keys():
        if k1 in dic2:
            lista_vazia.append(k1)
    return lista_vazia