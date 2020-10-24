def traduz(lista, dicionario):
    nova = []
    for chave in dicionario:
        if chave in lista:
            nova.append(dicionario[chave])
    return nova