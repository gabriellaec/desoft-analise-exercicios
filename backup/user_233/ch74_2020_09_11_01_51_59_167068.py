
def conta_bigramas(string):
    
    bigramas = dict()
    caractere_anterior = string[0]
    
    for caractere in string[1:]:
        
        print(caractere)
        
        bigrama = caractere + caractere_anterior
        caractere_anterior = caractere
        
        if bigrama not in bigramas.keys():
            bigramas[bigrama] = 1
            continue
            
        bigramas[bigrama] += 1
   
    return bigramas
    
    