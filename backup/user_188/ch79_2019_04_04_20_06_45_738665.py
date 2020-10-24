def monta_dicionario(lista1, lista2):
    dicionario = {}
    for numero in range(len(lista1)):
        dicionario[lista1[numero]] = lista2[numero]
    return dicionario
    