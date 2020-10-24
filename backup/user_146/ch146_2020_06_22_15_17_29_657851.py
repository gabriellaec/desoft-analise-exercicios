def conta_ocorrencias(lista):
    dicionario = {}
    for e in lista:
        if e in dicionario:
            dicionario += 1
        else:
            dicionario = 1
    print(dicionario)