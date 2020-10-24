def verifica_progressao(lista):
    contadorpa = 0
    contadorpg = 0
    contadorpaepg = 0

    for i in range(0, len(lista) - 2):
        if lista[i + 2] - lista[i + 1] == lista[i + 1] - lista[i] and lista[i + 2] / lista[i + 1] == lista[i + 1] / lista[i]:
            contadorpaepg += 1
        elif lista[i + 2] - lista[i + 1] == lista[i + 1] - lista[i]:
            contadorpa += 1
        elif lista[i + 2] / lista[i + 1] == lista[i + 1] / lista[i]:
            contadorpg += 1

    if contadorpa == len(lista) - 2:
        return 'PA'
    elif contadorpg == len(lista) - 2:
        return 'PG'
    elif contadorpaepg == len(lista) - 2:
        return 'AG'
    else:
        return 'NA'