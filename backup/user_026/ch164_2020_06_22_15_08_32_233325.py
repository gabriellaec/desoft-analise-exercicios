def traduz(lista, dic):
    tradução= []
    for i in lista:
        traduzido = dic[i]
        tradução.append(traduzido)
    return(tradução)