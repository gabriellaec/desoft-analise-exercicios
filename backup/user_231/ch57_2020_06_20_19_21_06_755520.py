def verifica_progressao(lista):
    i=0
    for i in range(len(lista)):
        if lista[i]+lista[i+1]==lista[i+2] and lista[i]*lista[i+1]==lista[i+2]:
            return 'AG'
        elif lista[i]+lista[i+1]==lista[i+2]:
            return 'PA'
        elif lista[i]*lista[i+1]==lista[i+2]:
            return 'PG'
        else:
            return 'NA'
        
        