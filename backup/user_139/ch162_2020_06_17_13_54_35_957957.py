def verifica_lista (lista):
    if lista == []:
        return 'misturado'
    for i in len(lista):
        if lista[i] %2 == 0:
            return 'par'
        elif lista[i] %2 != 0:
            return 'ímpar'
        else:
            return 'misturado'