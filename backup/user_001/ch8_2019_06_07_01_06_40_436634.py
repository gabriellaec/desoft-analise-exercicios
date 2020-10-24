def verifica_progressao(lista):
    i = 0
    r = lista[i] - lista[i+1]
    q = lista[i]/lista[i+1]
    while i + 2 < len(lista):
        if lista[i+1]-lista[i+2] == r:
            return 'PA'
        elif lista[i+1]/lista[i+2] == q:
            return 'PG'
        elif lista[i+1]-lista[i+2] == r and lista[i+1]/lista[i+2] == q:
            return 'AG'
        else:
            return 'NA'
        i += 1