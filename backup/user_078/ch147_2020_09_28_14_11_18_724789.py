def mais_frequente(lista):

    dicionario_palavras = conta_ocorrencias(lista)
    i=0
    maior = dicionario_palavras[0]

    while i < len(dicionario_palavras):
        
        if dicionario_palavras[i+1] > dicionario_palavras[i]:
            maior = dicionario_palavras[i].keys()        
        i+=1
    
    return maior