def interseccao_chaves(dic1, dic2):
    inter = []
    for chave in dic1.keys():
        if chave in dic2.keys():
            inter.append(chave)
    return inter