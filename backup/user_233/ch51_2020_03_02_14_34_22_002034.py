def primos_entre(a,b):
    
    for i in range(a, b + 1):
        
        numeros_primos = list()
        
        if i == 0 or i == 1: continue
            
        if i == 2: 
            numeros_primos.append(i)
            continue
            
        if i % 2 == 0: continue
        
        divisor = 3
        
        while True:
            
            if divisor == i:
                numeros_primos.append(i)
                continue
                
            if i % divisor == 0: continue
            
            divisor += 2
       
    	if i == b: return numeros_primos
            
            
            
            