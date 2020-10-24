def primos_entre(a, b):
    p = 0
    i = a
    ímpares = 3
    while i <= b:
        if i == 1:           
           i += 1
        
        elif i == 2 or i == 3:
           p += 1
           i += 1
                   
        else:
            if i % 2 == 0:
               i += 1
            
            else: 
                
                while i % ímpares != 0 and ímpares < i:
                    ímpares += 2
                
                if i == ímpares and i % ímpares == 0:
                    p += 1
                    i += 1
                    ímpares = 3
                else:
                    p += 1
                    i += 1
                    ímpares = 3
            
    return p