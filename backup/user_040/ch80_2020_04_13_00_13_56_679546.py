def interseccao_chaves(x,y):
    n = 0
    lista = []
    for chave in x.key:
        if chave == y[n].key:
            lista.append(chave)
            lista.append(y[n].key)
        n+=1