def conta_ocorrencias (lista):
    i = 0
    dicionario = {}
    while i < len(lista):
        if lista[i] in dicionario:
            values = lista.count(lista[i])
            dicionario[lista[i]] = values
        else:
            dicionario[lista[i]] = 1
        i = i + 1
    return dicionario

def mais_frequentes (dicionario):
    valores=dicionario.values()
    return max(dicionario)