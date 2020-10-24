def verifica_progressao(lista):
    # Verifica se é PA
    i = 1
    while lista[i] - lista[i - 1] == lista[1] - lista[0] and i < (len(lista) - 1):
        i += 1
    if i == (len(lista) - 1):
        return 'PA'
    else:
        # Verifica se é PG
        i = 1
        while (lista[i]/lista[i - 1]) == (lista[1]/lista[0]) and i < (len(lista) - 1):
            i += 1
        if i == (len(lista) - 1):
            return 'PG'
        def verifica_progressao(lista):
    # Verifica se é PA
    i = 1
    while lista[i] - lista[i - 1] == lista[1] - lista[0] and i < (len(lista) - 1):
        i += 1
    if i == (len(lista) - 1):
        return 'PA'
    else:
        # Verifica se é PG
        i = 1
        while (lista[i]/lista[i - 1]) == (lista[1]/lista[0]) and i < (len(lista) - 1):
            i += 1
        if i == (len(lista) - 1):
            return 'PG'
        else:
            # Verifica se é PAG
            i = 1
            while lista[i] - lista[i - 1] == lista[1] - lista[0] and (lista[i]/lista[i - 1]) == (lista[1]/lista[0]) and i < (len(lista) - 1):
                i += 1
            if i == (len(lista) - 1):
                return 'AG'
            else:
                # Confirma que não é nenhum caso acima
                return 'NA':
            # Verifica se é PAG
            i = 1
            while lista[i] - lista[i - 1] == lista[1] - lista[0] and (lista[i]/lista[i - 1]) == (lista[1]/lista[0]) and i < (len(lista) - 1):
                i += 1
            if i == (len(lista) - 1):
                return 'AG'
            else:
                # Confirma que não é nenhum caso acima
                return 'NA'