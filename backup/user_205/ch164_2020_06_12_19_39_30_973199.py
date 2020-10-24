def traduz(lista,dicionario):
    trad = []
    for i in range(len(lista)):
        palavra = lista[i]
        for chave in dicionario:
            if chave == palavra:
                trad.append(dicionario[chave])
    return trad
            