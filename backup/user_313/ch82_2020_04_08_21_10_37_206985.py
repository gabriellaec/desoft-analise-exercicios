def  primeiras_ocorrencias(a):

    dicionario = {}
    for i in range (0,len(a)-1):
        if a[i] not in dicionario:
            z = a[i]
            dicionario[a[i]] = i
        

    return(dicionario)