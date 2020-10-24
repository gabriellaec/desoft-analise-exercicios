def conta_ocorrencias(lista):
    dicionario = dict()
    for i in lista:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    return dicionario

def mais_frequente(lista, conta_ocorrencias(lista)):
    for i in lista:
        if dicionario[i] > dicionario[i-1]:
            dicionario[i] = maior
    return maior