def conta_ocorrencias(lista):
    dic= {}
    for palavra in lista:
        dic[palavra] = lista.count(palavra)
    return dic

def mais_frequente(lista):
    dicionario = {}
    a = conta_ocorrencias(dicionario)
    valores = a.values()
    mais_freq = max(valores)
    if mais_freq in a:
        return a[mais_freq]
        