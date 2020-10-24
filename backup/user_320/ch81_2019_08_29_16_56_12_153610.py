def interseccao_valores(dic1, dic2):
    inter = []
    for chave in dic1.values():
        if chave in dic2.values():
            inter.append(chave)
    return inter