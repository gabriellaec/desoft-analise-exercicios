def interseccao_chaves(dicionario_1, dicionario_2):
    lista_chave_1 = []
    lista_chave_2 = []
    for chaves_1 in dicionario_1.keys():
        lista_chave_1.append(chaves_1)
    for chaves_2 in dicionario_2:
        lista_chave_2.append(chaves_2)
    lista_final = []
    i = 0
    while i < len(lista_chave_1):
        if lista_chave_2[i] in lista_chave_1:
            lista_final.append(lista_chave_2[i])
        i += 1
    return lista_final