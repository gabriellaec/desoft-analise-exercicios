def verifica_progressao(lista):
    i = 0
    r = lista[i+1] - lista[i]
    q = lista[i+1]/lista[i]
    while i + 2 < len(lista):
        if lista[i+1]-lista[i] == r:
            return 'PA'
        elif lista[i+1]/lista[i] == q:
            return 'PG'
        elif lista[i+1]-lista[i] == r and lista[i+1]/lista[i] == q:
            return 'AG'
        else:
            return 'NA'