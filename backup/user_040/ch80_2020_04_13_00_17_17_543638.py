def interseccao_chaves(x,y):
    n = 0
    lista = []
    for chave in x.keys():
        if chave == y.keys():
            lista.append(chave)
    return lista