def conta_ocorrencias(lista):
    dicio = {}
    for i in lista:
        if i not in dicio:
            dicio[i] = 1
        else:
            dicio[i] +=1
    return dicio
def mais_frequente(lista):
    x = conta_ocorrencias(lista)
    mais = 0
    for i,n in x.items():
        if n > mais:
            palavra = i
    return palavra