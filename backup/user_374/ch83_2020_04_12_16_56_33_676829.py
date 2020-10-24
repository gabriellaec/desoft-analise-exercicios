def medias_por_inicial(l1):
    dicicionario = {}
    for k, v in l1.items():
       
        a = k
        b = v
        
        if a[0] not in dicicionario:
            dicicionario[a[0]] = b
        else: 
            dicicionario[a[0]] = (dicicionario[a[0]]+b)/2
    return dicicionario
