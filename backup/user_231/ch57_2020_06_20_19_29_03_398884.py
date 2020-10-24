def verifica_progressao(lista):
    i=0
    r= lista[i+1]-lista[i]
    while i< len(lista):
        if lista[i]+r==lista[i+1] and lista[i]*r==lista[i+1]:
            return 'AG'
        elif lista[i]+r==lista[i+1]:
            return 'PA'
        elif lista[i]*r==lista[i+1]:
            return 'PG'
        else:
            return 'NA'
        
        