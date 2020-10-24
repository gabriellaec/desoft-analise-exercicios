def maior_primo_menor_que(n):
    i = 0
    numero = 1
    
    if n < 2:
        return -1
    
    else:
        while numero <= n:
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
    
def n_primo(n):
    ímpares = 3
    if n == 1:           
       return False
        
    elif n == 2 or n == 3:
        return True
                   
    else:
       if n % 2 == 0:
          return False
                
       else: 
                    
           while n % ímpares != 0 and ímpares < n:
               ímpares += 2
               
           if n == ímpares and n % ímpares == 0:
              return True
                    
           else:
              return False