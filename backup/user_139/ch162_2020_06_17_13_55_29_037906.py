def verifica_lista (lista):
    if lista == []:
        return 'misturado'
    for i in range(len(lista)):
        if lista[i] == 0 or lista[i] %2 == 0:
            return 'par'
        elif lista[i] == 1 or lista[i] %2 != 0:
            return 'ímpar'
        else:
            return 'misturado'