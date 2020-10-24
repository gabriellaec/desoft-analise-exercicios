with open('churras.txt','r') as churras:
    
    for a in churras.readlines():
        a.split(',')
        for b in a.split(','):
            quant=float(b[1])
            valor=float(b[2])
            consumo+=quant*valor
print(consumo)
            
                
            	
         
                
        
	