def interseccao_chaves(x,y):
    n = 0
    lista = []
    for chave in x.keys():
        if chave == y[n].keys():
            lista.append(chave)
            lista.append(y[n].keys())
        n+=1