def conta_ocorrencias(lista):
    a = len(lista)
    dic= {}
    for palavra in range(a):
        if not palavra in dic:
            dic[palavra] = 1
        else:
            dic[palavra] += 1
    return dic
            
        
        
        