def interseccao_chaves(x,y):
    n = 0
    lista = []
    for chave in x:
        lista.append(chave.value)
        lista.append(y[n].value)
        n+=1