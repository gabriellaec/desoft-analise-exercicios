def verifica_lista(lista):
    j = 0
    p = 0
    i = 0
    if lista == []:
        return 'misturado'

    while j < len(lista):
        if lista[j]%2 == 0:
            p += 1
            if p == len(lista):
                return 'par'
        elif lista[j]%2 != 0:
            i += 1
            if i == len(lista):
                return 'ímpar'
        j += 1

    return 'misturado'
        
        