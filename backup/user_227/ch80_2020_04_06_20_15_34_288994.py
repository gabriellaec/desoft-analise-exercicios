def interseccao_chaves(dic1, dic2):
    lista_chaves=[]
    for chave in dic1:
        if chave in dic2:
            lista_chaves.append(chave)
    return lista_chaves