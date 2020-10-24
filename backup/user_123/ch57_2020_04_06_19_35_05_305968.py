def verifica_progressao (lista):
    lista2 = []
    i = 0
    while i < len(lista):
        if (lista[i+1] - lista [i]) == (lista [i+2] - lista [i+1]):
            return ('PA')
        elif (lista[i+1]/lista[i]) == (lista[i+2]/lista[i+1]):
            return ('PG')
        elif (lista[i+1]/lista[i]) == (lista[i+2]/lista[i+1]) and (lista[i+1] - lista [i]) == (lista [i+2] - lista [i+1]):
            return ('AG')
    i += 1
    
        
 