def verifica_progressao (lista):
    i=2
    while i<len(lista):
        if lista[i+2]-lista[i+1]==lista[i+1]-lista[i] and lista[i+2]/lista[i+1]==lista[i+1]/lista[i]:
            s= 'AG'
        elif lista[i+2]-lista[i+1]==lista[i+1]-lista[i]:
            s= 'PA'
        elif lista[i+2]/lista[i+1]==lista[i+1]/lista[i]:
            s= 'PG'    
        else:
            s= 'NA'
        i+=1
    return s
    