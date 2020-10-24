def monta_dicionario (lista1, lista2):
    dicionario = {}
    for i in range(len(lista1)):
        chave = lista1[i]
        valor = lista2[i]
        dicionario [chave] = valor
    return dicionario