def calcula_total_da_nota (preco,quant):
    s=0
	i=0
	while i < len(preco):
        y= preco[i]*quant[i] 
        i+=1
        s+=y
    return s
        
       
   	
  
    
    