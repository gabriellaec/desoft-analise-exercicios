def verifica_progressao(lista):
    i=0
    while len(lista) >= 2 and i < len(lista):
        if lista[i+1] - lista[i] == lista[i+2] - lista[i+1]:
            i+=1
            return 'PA'
        elif lista[i+1] / lista[i] == lista[i+2] / lista[i+1] and lista[i] != 0 and lista[i+1] != 0:
            i+=1
            return 'PG'
        elif lista[i+1] - lista[i] == lista[i+2] - lista[i+1] and lista[i+1] / lista[i] == lista[i+2] / lista[i+1] and lista[i] != 0 and lista[i+1] != 0:
            return 'AG'
        else:
            return 'NA'