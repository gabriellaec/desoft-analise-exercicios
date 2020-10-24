def conta_ocorrencias(lista):
    dicionario = dict()
    lista_numeros = []
    for i in range(0, len(lista)):
        lista_numeros.append(i + 1)
    i = 0
    while i < len(lista):
        dicionario[lista[i]] = lista_numeros[i]
        i += 1
    return dicionario