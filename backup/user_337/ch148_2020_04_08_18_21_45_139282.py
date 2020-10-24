def conta_letras(lista):
    dicionario = {}
    for palavra in lista:
        if not palavra in dicionario:
            dicionario[palavra] = 1
        else:
            dicionario[palavra]+=1
    return dicionario
