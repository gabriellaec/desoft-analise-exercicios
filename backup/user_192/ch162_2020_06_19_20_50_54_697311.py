def verifica_lista(x):
    par = []
    impar = []
    for i in range(len(x)):
        if x[i] % 2 == 0:
            par.append(x[i])
        elif x[i] % 2 != 0:
            impar.append(x[i])
    if x == []:
        return 'misturado'
    elif impar == []:
        return 'par'
    elif par == []:
        return 'ímpar'
    else:
        return 'misturado'