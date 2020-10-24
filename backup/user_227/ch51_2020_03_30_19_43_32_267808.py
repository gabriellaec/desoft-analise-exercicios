def primos_entre(a, b):
    primos = []
    numero = a
    while numero <= b:
        ímpares = 3
        if numero == 1:           
           numero += 1
        
        elif numero == 2 or numero == 3:
           primos.append(numero)
           numero += 1
                   
        else:
            if numero % 2 == 0:
               numero += 1
            
            else: 
                
                while numero % ímpares != 0 and ímpares < numero:
                    ímpares += 2
                
                if numero == ímpares and numero % ímpares == 0:
                    primos.append(numero)
                    ímpares = 3
                    numero += 1
                else:
                    numero += 1
                    ímpares = 3
                    
    return primos