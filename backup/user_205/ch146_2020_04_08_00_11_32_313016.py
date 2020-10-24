def conta_ocorrencias(lista): 
    dic={}
    for palavras in lista:
        dic[palavras]=lista.count(palavras)
    return dic
        
            
            
        