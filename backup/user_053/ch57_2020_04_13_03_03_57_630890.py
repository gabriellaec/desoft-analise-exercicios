def verifica_progressao(lista):
    # Verifica se é PA
    i = 1
    while i < len(lista) and lista[i] - lista[i - 1] == lista[1] - lista[0]:
        i += 1
    if i == len(lista):
        # Verifica se tem termo 0
        condicao = True
        for numero in lista:
            if numero == 0:
                condicao = False
                return 'PA'
        # Verifica se é PG e, consequentemente, AG
        if condicao:
            i = 1
            while i < len(lista) and (lista[i]/lista[i - 1]) == (lista[1]/lista[0]):
                    i += 1
                if i == (len(lista)):
                    return 'AG'
                else:
                    return 'PA'
    # Não é PA. Verifica se é PG
    else:
        i = 1
        for numero in lista:
            if numero == 0:
                return 'NA'
            else:
                while i < len(lista) and (lista[i]/lista[i - 1]) == (lista[1]/lista[0]):
                    i += 1
                if i == (len(lista)):
                    return 'PG'