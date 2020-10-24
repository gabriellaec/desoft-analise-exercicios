def zera_negativos(lista):
    i=0
    vp =[]
    if lista[i] == 0:
        vp.append(0)
    else:
    
    	while i<len(lista):
        	if lista[i]>0:
           		vp.append(lista[i])
        	i+=1  
        
            
    return vp