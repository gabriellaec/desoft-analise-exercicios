def conta_ocorrencias(lista):
    dicionario = {}
    k = dicionario.keys()
    for i in range (0, len(lista)):
        if lista[i] not in k:
            contador = lista.count(lista[i])
            dicionario[lista[i]]=contador
    n = 0
    palavra = ' '
    for c,v in dicionario.items():
        if v > n:
            n = v
            palavra = c
    return palavra