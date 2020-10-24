def conta_ocorrencias(lista):
    dicionario = {}
    for i in lista:
        if i in dicionario:
            dicionario [i] += 1
        elif i not in dicionario: 
            dicionario [i] = 1
    return dicionario

def mais_frequente(lista):
    y = 0
    for i,x in conta_ocorrencias(lista):
        if x>y:
            palavra = i
            y = x
    return palavra