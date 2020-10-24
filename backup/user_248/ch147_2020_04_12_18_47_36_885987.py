def conta_ocorrencias(lista):
    dicionario=dict()
    for e in lista:
        if not e in dicionario:
            dicionario[e]=1
        else:
            dicionario[e]+=1
    return dicionario
def mais_frequente(dicionario):
    maior=dicionario.value{0}
    for val in dicionario.value:
        maior=val
    return maior
        