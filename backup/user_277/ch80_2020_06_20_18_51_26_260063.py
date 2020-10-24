def interseccao_chaves(dicionario1, dicionario2):
    lista1 = []
    lista2 = []
    lista_final = []
    for chave1 in dicionario1:
        lista1.append(chave1)
    for chave2 in dicionario2:
        lista2.append(chave2)
    for i in len(lista1):
        if lista1[i] == lista2[i]:
            lista_final.append(lista1[i])
    return lista_final
        