def verifica_progressao(lista):
    i=0
    
    while i < len(lista):
        if lista[i+1]/lista[i]==lista[i+2]/lista[i+1]:
            return "PG"
        	i=i+1
            if lista[i+1]-lista[i]==lista[i+2]-lista[i+1]:
            	return "AG"
                i+=1
       	if lista[i+1]-lista[i]==lista[i+2]-lista[i+1]:  
            return "PA"
        	i+=1
        else:
            return "NA"
            i+=1
        
        
   