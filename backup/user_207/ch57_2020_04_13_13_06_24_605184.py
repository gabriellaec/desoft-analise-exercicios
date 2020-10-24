def verifica_progressao (lista):
    razao = lista[-2] - lista[-1]
    quociente = lista[-2]/lista[-1]
    r = lista[1] - lista[0]
    q = lista[1]/lista[0]
    resultado = ''

    if r == razao:
        resultado = 'PA'
    elif q == quociente:
        resultado = 'PG'
    elif r == q and razao == quociente and quociente == r:
        resultado = 'AG'
    else:
        resultado = 'NA'
    return resultado