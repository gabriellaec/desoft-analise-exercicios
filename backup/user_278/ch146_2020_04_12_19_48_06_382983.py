def conta_ocorrencias(palavras):
    ocorrencias = {}
    k = ocorrencias.keys()
    for i in range (0,len(palavras)):
        if palavras[i] not in k:
            contador = palavras.count(palavras[i])
            ocorrencias [palavras[i]] = contador
    return ocorrencias