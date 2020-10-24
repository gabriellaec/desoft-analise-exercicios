def primeiras_ocorrencias(palavra):
    
    caracteres = {}
    
    i = 0
    
    for e in palavra:
        
        if not e in caracteres:
            caracteres[e] = i
        
        i += 1
    
    return caracteres
            
    