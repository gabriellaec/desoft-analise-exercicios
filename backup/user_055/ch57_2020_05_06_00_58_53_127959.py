def verifica_progressao(lista_numeros):
    if len(lista_numeros) < 3:
        return 'NA'
    for i in range(len(lista_numeros) - 3):
        if (lista_numeros[i + 1] - lista_numeros[i]) == (lista_numeros[i + 2] - lista_numeros[i + 1]):
            PA = True
        if (lista_numeros[i + 1] / lista_numeros[i]) == (lista_numeros[i + 2] / lista_numeros[i + 1]):
            PG = True
    if PG and PA == True:
        return 'AG'
    
    else:
        if PA == True:
            return 'PA'
        if PG == True:
            return 'PG'
        else:
            return 'NA'
            
        
        
        