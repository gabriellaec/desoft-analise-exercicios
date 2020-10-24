def verifica_progressao(lista):
    i=0
    while i<len(lista):
        if lista[i-1]*lista[i+1]==(lista[i])**2:
            return 'PG'
        elif lista lista[i-1]+lista[i+1]=2*lista[i]:
            return 'PG'
        elif lista[i-1]*lista[i+1]==(lista[i])**2 and lista lista[i+1]+lista[i-1]=2*lista[i]:
            return'AG'
        else:
            return 'NA'