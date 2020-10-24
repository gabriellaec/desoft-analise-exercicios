def interseccao_chaves(x,y):
    lista = []
    for chave in x.keys():
        for chave2 in y.keys():
            if chave == chave2:
                lista.append(chave)
    return lista