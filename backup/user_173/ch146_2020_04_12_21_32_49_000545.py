def conta_ocorrencias (lista):
    dicionario = {}
    for i in lista:
        dicionario [i] = lista.count(i)
    
    return dicionario