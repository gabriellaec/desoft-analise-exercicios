def conta_ocorrencias (lista):
    dicionario = {}
    for i in lista:
        if i in dicionario:
            dicionario [i] += 1
        elif i not in dicionario: 
            dicionario [i] = 1
    return dicionario
         