def conta_ocorrencias(lista):
    dicionario = {}
    for palavra in lista:
        if not palavra in dicionario:
            dicionario[palavra] = 1
        else:
            dicionari[palavra]+=1
    return dicionario