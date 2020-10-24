
def verifica_lista(lista):
    
    resultado = 0    # BANDEIRA DE ELEMENTOS PARES OU ÍMPARES ANTERIORES
                     # (0 para indefinido, 1 para ímpar, 2 para par)
        
    for elemento in lista:
        
        if elemento % 2 == 0:    # PAR
            
            if resultado == 0:
                resultado = 2
                continue
                
            if resultado == 1:
                return 'misturado'
            
            else: continue
        
        else:                    # ÍMPAR
            
            if resultado == 0:
                resultado = 1
                continue
                
            if resultado == 2:
                return 'misturado'
    
    if resultado == 1: return 'ímpar'
    if resultado == 2: return 'par'
    else: return 'misturado'
    