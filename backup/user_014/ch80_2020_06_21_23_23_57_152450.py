def interseccao_chaves(dicionario_1, dicionario_2):
    lista = []
    for chaves_1 in dicionario_1.keys():
        lista.append(chaves_1)
    for chaves_2 in dicionario_2:
        if chaves_2 not in lista:
            lista.append(chaves_2)
    return lista