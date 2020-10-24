def verifica_progressao (lista):
    i=1
    while i<len(lista):
        if lista[i]-lista[i-1]==lista[i+1]-lista[i] and lista[i]/lista[i-1]==lista[i+1]/lista[i]:
            s= 'AG'
        elif lista[i]-lista[i-1]==lista[i+1]-lista[i]:
            s= 'PA'
        elif lista[i]/lista[i-1]==lista[i+1]/lista[i]:
            s= 'PG'    
        else:
            s= 'NA'
        i+=1
    return s
    