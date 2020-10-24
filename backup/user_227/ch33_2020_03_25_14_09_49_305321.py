def primos_entre(a, b):
    p = 0
    i = a
    while i <= b:
        if i == 1:           #para i == 11 e p == 4
           i += 1
        
        elif i == 2 or i == 3:
           p += 1
           i += 1
                   
        else:
            ímpares = 3
            if i % 2 == 0:
                i += 1
            
            else: 
                while ímpares < i and i % ímpares != 0 :                    
                    ímpares += 2
                
                else:
                    p += 1
                    i += 1
                     
    return p