def verifica_lista(x):
    for i in range(len(x)):
        if x[i] % 2 == 0:
            return 'par'
        elif x[i] % 2 != 0:
            return 'ímpar'
        elif x[i] % 2 == 0 and x[i] % 2 != 0:
            return 'misturado'
        elif x == []:
            return 'misturado'