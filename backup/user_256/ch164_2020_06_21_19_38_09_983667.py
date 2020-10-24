def traduz(lista, dicionario):
    nova = []
    for chaves in dicionario.keys():
        if chaves in lista:
            nova.append(dicionario.values())
    return nova