'''def medias_por_inicial(l1):
    dicionario = {}
    dic2 = {}
    for k, v in l1.items():
       
        a = k
        b = v
        if a[0] not in dicionario:
            dicionario[a[0]] = b
            dic2[a[0]] = 1
            
            
        else: 
            dicionario[a[0]] = (dicionario[a[0]]+b)
            dic2[a[0]] += 1
    
    for k in dicionario:
        dicionario[k]= dicionario[k]/dic2[k]
    
    return dicionario'''
        
    
def medias_por_inicial(dicionario):
    notas = {}
    contagem = {}

    for inicial in dicionario:
        if inicial[0] not in notas:
            notas[inicial[0]] = dicionario[inicial]
            contagem[inicial[0]] = 1
        else:
            notas[inicial[0]] += dicionario[inicial]
            contagem[inicial[0]] += 1
        
    for key in notas:
        notas[key] = notas[key]/contagem[key] 
    
    return notas