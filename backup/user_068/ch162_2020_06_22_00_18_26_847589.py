
def verifica_lista(lista):
    if len(lista) != 0:
        if lista[0]%2 == 0:
            for i in lista:
                if i%2 == 1:
                    return 'misturado'
            return 'par'
        if lista[0]%2 == 1:
            for i in lista:
                if i%2 == 0:
                    return 'misturado'
            return 'ímpar'
    else:
        return 'misturado'