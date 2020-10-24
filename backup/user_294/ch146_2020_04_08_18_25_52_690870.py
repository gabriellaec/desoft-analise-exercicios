def conta_ocorrencias(lista):
    dicionario={}
    i=0
    for i in lista:
        if not i in dicionario:
            dicionario[i]=1
        else:
            dicionario[i]+=1
            
    return dicionario