def conta_ocorrencias(lista):
    dicionario = dict()
    for i in lista:
        contador = 0
        j = 0
        while j < len(lista):
            if lista[j] == i:
                contador += 1
                j += 1
            else:
                j += 1
        dicionario[i] = contador
    return dicionario