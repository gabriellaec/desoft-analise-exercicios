def primeiras_ocorrencias(palavra):
    dicionario={}
    cont=0
    for i in palavra:
        if i not in dicionario:
            dicionario[i]=cont
        
        cont+=1
    return dicionario