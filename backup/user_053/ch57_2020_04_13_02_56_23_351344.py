def verifica_progressao(lista):
    # Verifica se é PA
    i = 1
    while i < len(lista) and lista[i] - lista[i - 1] == lista[1] - lista[0]:
        i += 1
    if i == len(lista):
        # Verifica se é PG e, consequentemente, AG
        i = 1
        for numero in lista:
            if numero != 0:
                while i < len(lista) and (lista[i]/lista[i - 1]) == (lista[1]/lista[0]):
                    i += 1
                if i == (len(lista)):
                    return 'AG'
                else:
                    return 'PA'
            else:    
                return 'PA'
    else:
        # Verifica se é PG
        i = 1
        for numero in lista:
            if numero == 0:
                return 'NA'
            else:
                while i < len(lista) and (lista[i]/lista[i - 1]) == (lista[1]/lista[0]):
                    i += 1
                if i == (len(lista)):
                    return 'PG'