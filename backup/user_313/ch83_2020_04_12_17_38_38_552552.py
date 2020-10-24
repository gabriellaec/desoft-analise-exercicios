def medias_por_inicial(l1):

    dicionario = {}
    novalista= []

    for k, v in l1.items():
        
        a = k
        b = v
        
        if a[0] not in dicionario:
            dicionario[a[0]] = b

        else:
            dicionario[a[0]] = (dicionario[a[0]]+b)/2

    return dicionario