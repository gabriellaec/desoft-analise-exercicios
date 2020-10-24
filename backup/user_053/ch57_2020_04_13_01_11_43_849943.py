def verifica_progressao(lista):
    # Verifica se é PA
    i = 1
    while i < len(lista) and lista[i] - lista[i - 1] == lista[1] - lista[0]:
        i += 1
    if i == len(lista):
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
                else:
                    # Verifica se é PAG
                    i = 2
                    for numero in lista:
                        if numero == 0:
                            return 'NA'
                        else:
                            while i < len(lista) and lista[i] - lista[i-1] == lista[i-1] - lista[i-2] and lista[i]/lista[i-1] == lista[i-1]/lista[i-2]:
                                i += 1
                            if i == (len(lista)):
                                return 'AG'
                            else:
                                # Confirma que não é nenhum caso acima
                                return 'NA'