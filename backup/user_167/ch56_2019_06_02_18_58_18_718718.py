def calcula_total_da_nota (preco,quantidade):
    s=0
	i=0
	while i < len(preco):
        y= preco[i]*quantidade[i] 
        i+=1
        s+=y
    return s
        
       
   	
  
    
    