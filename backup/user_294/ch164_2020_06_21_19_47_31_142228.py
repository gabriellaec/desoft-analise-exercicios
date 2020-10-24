def traduz (lista, dicionario):
    nova = []
    for palavra in lista:
        for chaves in dicionario:
            if palavra == chave:
                nova.append(dicionario[chave])
    return nova