def verifica_progressao(lista):
    i = 0
    while i < len(lista):
        if lista[i+1] - lista[i] == lista[1+2] - lista[1+1]:
        	return 'PA'
        elif lista[i+1] == lista[i]*(lista[i+1] - lista[i]):
            return 'PG'
        elif lista[i+1] - lista[i] == lista[1+2] - lista[1+1] and elif lista[i+1] == lista[i]*(lista[i+1] - lista[i]):
            return 'AG'
        else:
            return 'NA'
    