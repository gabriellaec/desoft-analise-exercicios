def conta_ocorrencias (lista):
    dicionario = {lista}
    i = 0 
    while i < len(lista):
        dicionario[i] = lista[i]
        i += 1
    return dicionario
        