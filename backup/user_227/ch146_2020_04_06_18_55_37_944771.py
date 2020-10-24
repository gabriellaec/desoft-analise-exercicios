def conta_ocorrencias(lista):
    dicionario={}
    for palavra in lista:
        dicionario[palavra]=dicionario.count(palavra)
    return dicionario