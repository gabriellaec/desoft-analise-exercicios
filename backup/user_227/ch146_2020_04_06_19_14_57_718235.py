def conta_ocorrencias(lista):
    dicionario={}
    for palavra in lista:
        if not palavra in dicionario:
            dicionario[palavra]=lista.count(palavra)
    return dicionario