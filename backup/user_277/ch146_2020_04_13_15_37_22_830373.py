def conta_ocorrencias(lista_1):
    dicionario={}
    for i in lista_1:
        if not i in dicionario:
            dicionario[i]=1
        else:
            dicionario[i]+=1
    return dicionario