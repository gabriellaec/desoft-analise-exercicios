def verifica_progressao(lista):
    i = 0
    s = 0
    while i < len(lista):
        s += lista[i]
        i = i + 1
    if s == len(lista)*lista[0]:
        return 'AG'
    elif s == len(lista)*(lista[0]+lista[len(lista)-1])/2:
        return 'PA'
    elif s == lista[0]*((lista[1]/lista[0])**len(lista) - 1)/((lista[1]/lista[0]) - 1):
        return 'PG'
    else:
        return 'NA'