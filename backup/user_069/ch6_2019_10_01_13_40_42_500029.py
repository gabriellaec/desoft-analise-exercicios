def encontra_maximo (matriz):   
    matriz = [linha1, linha2, linha3]    
    len(linha1) == len(linha2) == len(linha3)    
    comparador = linha1[0]   
    for e in linha1:        
        if e > comparador:        	
            comparador = e        	
        for e in linha2:            
            if e > comparador:              	
                comparador = e                	
            for e in linha3:                     
                if e > comparador       				
                   comparador = e   
    return e