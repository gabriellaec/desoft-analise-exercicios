def conta_ocorrencias(lista):
    
    dicionario = {}
    
    for palavra in lista:
        if palavra in dicionario.keys(): dicionario[palavra] += 1
        else: dicionario[palavra] = 1
    
    return dicionario