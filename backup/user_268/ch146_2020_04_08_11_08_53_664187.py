def conta_ocorrencias(lista):
    a = len(lista)
    dic= {}
    for palavra in range(a):
        if not palavra in dic:
            contagem[palavra] = 1
        else:
            contagem[palavra] += 1
    return dic
            
        
        
        