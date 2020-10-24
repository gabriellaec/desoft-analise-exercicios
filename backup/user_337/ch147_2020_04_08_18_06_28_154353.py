def conta_ocorrencias(lista):
    dicionario = {}
    for palavra in lista:
        if not palavra in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra]+=1
    return dicionario

def mais_frequente (lista):
    dicionario = {}
    for palavra in lista:
        if not palavra in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra]+=1
    a = dicionario.values[0]
    i = 1
    while i<len(dicionario.values):
        if dicionario.values[i]>a:
            a = dicionario.values[i]
        i += 1
    return a