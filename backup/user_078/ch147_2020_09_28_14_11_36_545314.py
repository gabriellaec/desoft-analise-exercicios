def conta_ocorrencias(lista):
    dicionario = {}

    for palavra in lista:
        if palavra not in dicionario.keys():
            ocorrencias = lista.count(palavra)
            dicionario[palavra] = ocorrencias

    return dicionario


def mais_frequente(lista):

    dicionario_palavras = conta_ocorrencias(lista)
    i=0
    maior = dicionario_palavras[0]

    while i < len(dicionario_palavras):
        
        if dicionario_palavras[i+1] > dicionario_palavras[i]:
            maior = dicionario_palavras[i].keys()        
        i+=1
    
    return maior