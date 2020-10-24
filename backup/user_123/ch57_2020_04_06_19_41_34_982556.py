def verifica_progressao (lista):
    lista2 = []
    i = 0
    while i < len(lista):
        if (lista[i+1] - lista [i]) == (lista [i+2] - lista [i+1]):
            return ('PA')
        elif (lista[i+1]/lista[i]) == (lista[i+2]/lista[i+1]):
            return ('PG')
        elif lista[i] == lista[0]*((lista[1]/lista[0])**([i]-1)) and (lista[i+1] - lista [i]) == (lista [i+2] - lista [i+1]):
            return ('AG')
        elif lista[i] == lista[0]*((lista[1]/lista[0])**([i]-1)):
            return 'PG'
    i += 1
    
        
 