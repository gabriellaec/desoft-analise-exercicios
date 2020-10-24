def conta_ocorrencias(lista):
    a = len(lista)
    dic= {}
    for i in range(a):
        if not lista[i] in dic:
            dic[i] = 1
        else:
            dic[i] += 1
    return dic
            
        
        
        