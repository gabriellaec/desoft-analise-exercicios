def conta_ocorrencias(lista):
    dicionario = dict()
    for i in lista:
        if i in dicionario:
            dicionario[i] += 1
        else:
            dicionario[i] = 1
    return dicionario

def mais_frequente(lista):
    var = conta_ocorrencias(lista)
    maior = -1
    palavra = ''
    for i in var:
        if var[i] > maior:
            palavra = i
            maior = var[i]
    return maior