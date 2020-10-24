def separa_trios(lista):
	cont=0
	i=0
	listobas=[]
    sobra=[]
	tot=len(lista)
	while i<=tot:
		if tot-i>2:
			listeras=[lista[i],lista[i+1],lista[i+2]]
			i+=3
			listobas.append(listeras)
		else:
			sobra.append(lista[i])
            i+=1
                         
            
            
	return listobas
        		
              	
                
                
            
            
        
        