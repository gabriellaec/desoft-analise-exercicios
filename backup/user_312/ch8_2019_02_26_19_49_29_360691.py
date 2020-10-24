def verifica_progressao(lista):
    if lista[2]-lista[1] == lista[-1]-lista[-2] & lista[2]/lista[1] == lista[-1]/lista[-2]:
        return 'AG'
    elif lista[2]/lista[1] == lista[-1]/lista[-2]:
        return 'PG'
    elif lista[2]-lista[1] == lista[-1]-lista[-2]:
    	return 'PA'
    else
    	return 'NA'