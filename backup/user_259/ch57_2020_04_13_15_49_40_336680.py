def verifica_progressao(lista):
    if len(lista) == 0: 
        return 'NA'
    if 0 in lista:
        return 'NA'
    for i in range(len(lista)-1):
        if (lista[i+1]-lista[i]) == (lista[i-1]-lista[i-2]):
            return 'PA'
        elif (lista[i+1]/lista[i]) == (lista[i-1]/lista[i-2]):
            return 'PG'
        elif (lista[i+1]-lista[i]) == (lista[i-1]-lista[i-2]) and (lista[i+1]/lista[i]) == (lista[i-1]/lista[i-2]):
            return 'AG'
        else:
            return 'NA'
            
    
