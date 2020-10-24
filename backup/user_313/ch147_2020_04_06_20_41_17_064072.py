def conta_ocorrencias (l1):
    dicionario = {}
    
    for i in l1:
        if i not in dicionario:
            dicionario[i]=1
            

        else:
            dicionario[i] = dicionario[i]+1
        
    frequente = max(dicionario, key=len)    
    
    return frequente
