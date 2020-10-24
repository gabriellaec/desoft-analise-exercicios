def acha_bigramas(palavra):
    
    lista = []
    
    i = 0 
    
    while i < (len(palavra)-1):
        
        x = palavra[i] + palavra[i+1]
        
        if not x in lista:
            
            lista.append(x)
                
        i += 1
        
    return lista
        
		
        
         
        
     
        
        