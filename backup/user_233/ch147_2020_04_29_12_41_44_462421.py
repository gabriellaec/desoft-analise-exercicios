def conta_ocorrencias(lista):
    
    dicionario = {}
    
    for palavra in lista:
        if palavra in dicionario.keys(): dicionario[palavra] += 1
        else: dicionario[palavra] = 1
    
    return dicionario



def inverte_dicionario(dicionario):
    
    invertido = {}
    
    for chave in dicionario.keys():
        invertido[dicionario[chave]] = chave
    
    return invertido



def mais_frequente(lista):
    
    contagem = inverte_dicionario(conta_ocorrencias(lista))
    
    maximo = max(contagem.keys())
    return contagem[maximo]
    
    
    
    