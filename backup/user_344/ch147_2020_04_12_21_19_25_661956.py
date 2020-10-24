def conta_ocorrencias(lista):
    dic= {}
    for palavra in lista:
        dic[palavra] = lista.count(palavra)
    return dic

def mais_frequente(lista):
    dicionario = conta_ocorrencias(dic)
    valores = dicionario.values()
    mais_freq = max(valores)
        
        