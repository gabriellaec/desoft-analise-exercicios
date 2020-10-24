
def conta_bigramas(string):
    
    bigramas = dict()
    caractere_anterior = string[0]
    
    for caractere in string[1:]:
        
        bigrama = caractere + caractere_anterior
        
        if bigrama not in bigramas.keys():
            bigramas[bigrama] = 1
            continue
            
        bigramas[bigrama] += 1
   
    return bigramas
    
    