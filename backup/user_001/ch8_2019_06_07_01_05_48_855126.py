def verifica_progressao(lista):
    i = 0
    r = lista[i] - lista[i+1]
    q = lista[i]/lista[i+1]
    while i + 2 < len(lista):
        if lista[i]-lista[i+1] == r:
            return 'PA'
        elif lista[i]/lista[i+1] == q:
            return 'PG'
        elif lista[i]-lista[i+1] == r and lista[i]/lista[i+1] == q:
            return 'AG'
        else:
            return 'NA'
        i += 1