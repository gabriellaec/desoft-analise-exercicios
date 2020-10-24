def verifica_primos(lista):
    dicionario={}
    i=0
    while i<len(lista):
        lista[i]=numero
        ímpares = 3
        if numero == 1:           
            dicionario[numero]=False
            i += 1
        
        elif numero == 2 or numero == 3:
            dicionario[numero]=True
            i += 1
                   
        else:
            if numero % 2 == 0:
                dicionario[numero]=False
                i += 1
            
            else: 
                
                while numero % ímpares != 0 and ímpares < numero:
                    ímpares += 2
                
                if numero == ímpares and numero % ímpares == 0:
                    dicionario[numero]=True
                    i += 1
                else:
                    dicionario[numero]=False
                    i += 1
    return dicionario 