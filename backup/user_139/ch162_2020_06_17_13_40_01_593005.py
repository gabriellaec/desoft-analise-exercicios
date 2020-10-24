def verifica_lista (lista):
    for i in range(len(lista)):
        if lista[i] == lista []:
            return 'misturado'
        elif lista[i] %2 == 0:
            return 'par'
        elif lista[i] %2 != 0:
            return 'ímpar'
        else:
            return 'misturado'