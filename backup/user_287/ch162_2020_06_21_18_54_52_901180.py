def verifica_lista(X):
    X = []
    for i in range(len(X)):
        if X[i] % 2 === 0:
            return 'par'
        if X[i] % 2:
            return 'ímpar'
        else :
            return 'misturado'