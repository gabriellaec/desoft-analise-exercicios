def verifica_progressao (lista):
    i=1
    while i<len(lista):
        if lista[i+1]-lista[i]=lista[i]-lista[i-1]:
            s= 'PA'
        elif lista[i+1]/lista[i]=lista[i]/lista[i-1]:
            s= 'PG'
        elif lista[i+1]-lista[i]=lista[i]-lista[i-1] and lista[i+1]/lista[i]=lista[i]/lista[i-1]:
            s= 'AG'
        else:
            s= 'NA'
        
        i=i+1
        return s