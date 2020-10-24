def calcula_norma(vetor):
    
    i = 0
    
    squared = []
    
    norma = 0
    
    addition = 0
    
    while i < len(vetor):
        
        modulo = (vetor[i]**2)
        
        squared.append(modulo)
        
        i += 1
        
    for e in squared:
        
        addition += e
        
    norma = addition**(1/2)
    
    return norma
        
        
        
        