def verifica_lista(lista):
    lista = []
    for i in lista:
        if lista[i] %2 != 0:
            return 'impar'
        elif lista[i] %2 == 0:
            return 'par'
        else:
            return 'misturado'