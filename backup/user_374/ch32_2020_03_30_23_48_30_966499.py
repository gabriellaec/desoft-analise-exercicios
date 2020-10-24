def lista_primos(n):
   
    i = 1
    lista = []
    var = False
    
    while i < n:
        if i <= 1:
            var = False 
            
        elif i == 2:
            var =  True
            
        elif i%2 == 0:
            var = False
        
        k = 3
        while k < i :
            if i%k == 0:
                var = False           
            else:
                k = k + 2  
                var = True
    
    
    if var == True:
        lista.append(i) 
    
    i += 1  
    
    return lista
