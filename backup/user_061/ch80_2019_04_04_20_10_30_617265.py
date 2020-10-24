def interseccao_chaves(dict1,dict2):
    lista = []
    for chave1 in dict1.keys():
        for chave2 in dict2.keys():
            if chave1 == chave2:
                lista.append(chave1)
    return lista