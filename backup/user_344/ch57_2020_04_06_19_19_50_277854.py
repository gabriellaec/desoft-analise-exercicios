def verifica_progressao(lista):
    i= 0
    while i<len (lista):
        if (lista[i+1] - lista[i]) == (lista[i]- lista[i-1]):
            return 'PA'
        elif (lista[i+1] / lista[i]) == (lista[i] /lista[i-1]):
            return 'PG'
        elif (lista[i+1] - lista[i]) == (lista[i]- lista[i-1]) and (lista[i+1] - lista[i]) == (lista[i]- lista[i-1]):
            return 'AG'
        else:
            return 'NA'
        i+=1

