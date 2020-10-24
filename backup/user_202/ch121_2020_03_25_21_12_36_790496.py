def subtracao_de_listas(lista1, lista2):
    t1 = len(lista1)
    t2 = len(lista2)
    i = 0
    lista3 = []
    while i < t1: 
    	v = lista1[i]
        a = 0
    	while a < t2:
    		if v != lista2[a]:
    			lista3.append(v)
    			a += 1
    		else:
    			a += 1
    	i += 1
    return(lista3)
            
                
                
    
        
        