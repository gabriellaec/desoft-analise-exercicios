def maior_primo_menor_que(n):
    i = 0
    numero = 1
    
    if n < 2:
        return -1
    
    else:
        while numero < n:
            ímpares = 3
            if numero == 1:           
               numero += 1
            
            elif numero == 2 or numero == 3:
               i = numero
               numero += 1
                       
            else:
                if numero % 2 == 0:
                   numero += 1
                
                else: 
                    
                    while numero % ímpares != 0 and ímpares < numero:
                        ímpares += 2
                    
                    if numero == ímpares and numero % ímpares == 0:
                        i = numero
                        numero += 1
                        ímpares = 3
                    
                    else:
                        numero += 1
                        ímpares = 3
            
        return i