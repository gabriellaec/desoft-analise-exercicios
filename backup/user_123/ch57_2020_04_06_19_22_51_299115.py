def verifica_progressao(lista):
i=0
    while len(lista)>i:
        if (lista[i]-lista[i-1]) == (lista[i+1]-lista[i]):
            return 'PA'
        elif  (lista[i]/lista[i-1]) == (lista[i+1]/lista[i]):
            return 'PG'
        elif  (lista[i]/lista[i-1]) == (lista[i+1]/lista[i]) and (lista[i]-lista[i-1]) == (lista[i+1]-lista[i]):
            return 'AG'
        elif  (lista[i]/lista[i-1]) != (lista[i+1]/lista[i]) and (lista[i]-lista[i-1]) != (lista[i+1]-lista[i]):
            return 'NA'