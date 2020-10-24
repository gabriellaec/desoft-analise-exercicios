def verifica_progressao(lista):

    for n in range(len(lista) - 1):
        if (lista[n + 1] - lista[n]) == (lista[n-1] - lista[n-2]):
                return "PA"
        elif (lista[n + 1] / lista[n]) == (lista[n -1 ] / lista[n - 2]):
            return 'PG'
        else:
            return 'NA'
            