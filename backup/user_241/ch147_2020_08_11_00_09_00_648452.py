def conta_ocorrencias(lista):
    dicionario = {}
    for i in lista:
        x = lista.count(i)
        dicionario[i] = x
    return dicionario

def mais_frequente(lista):
    dicionario = conta_ocorrencias(lista)
    maiorc = 0
    maiornum = ''
    for item in lista:
        if dicionario[item] > maiorc:
            maiorc = dicionario[item]
            maiornum = item
    return maiornum
                               