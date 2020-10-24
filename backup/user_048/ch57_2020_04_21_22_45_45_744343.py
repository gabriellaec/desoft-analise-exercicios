def verifica_progressao(lista):
    variacao=lista[1]-lista[0]
    variacaog=lista[1]/lista[0]
    for e in range(len(lista)-1):
        if lista[e+1]-lista[e]==variacao:
            return 'PA'
        if lista[e+1]/lista[e]==variacaog:
            return 'PG'
        else:
            return 'NA'