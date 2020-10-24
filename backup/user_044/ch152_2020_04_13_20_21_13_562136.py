def verifica_preco(tit,dic,tab):
    cor=0
    preco=0
    for i,n in dic.items():
        if i==tit:
            cor=n
    for i,n in tab.items():
        if i==cor:
            preco=n
    return preco
            