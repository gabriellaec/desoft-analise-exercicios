def primeiras_ocorrencias (x):
    d={}
    posicao=0
    for e in x:
        if e not in d:
            posicao+=1
            d[e]=posicao
        return d
        
        
    
            
        