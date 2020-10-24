def conta_ocorrencias (lista):
    dicionario={}
    for palavra in lista:
        if palavra not in dicionario:
            dicionario[palavra]=1
        else:
            x=dicionario[palavra]+1
            dicionario[palavra]=x
    return dicionario