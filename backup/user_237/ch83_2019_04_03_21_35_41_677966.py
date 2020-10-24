def medias_por_inicial(dicionario):
    soma = {}
    aparicao_letras = {}
    media = {}
    for k,v in dicionario.items():
             
        if k[0] in soma:
            soma[k[0]] += v
            aparicao_letras[k[0]] += 1
          
        if k[0] not in soma:
            soma[k[0]] = v
            aparicao_letras[k[0]] = 1
            
    for q,w in aparicao_letras.items():
        
        media[q] = soma[q]/w
    
            
    return (media)
        
        
    
    