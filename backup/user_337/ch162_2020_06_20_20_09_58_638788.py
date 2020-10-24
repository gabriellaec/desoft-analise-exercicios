def verifica_lista(lista):
    p = 0
    i = 0
    if len(lista) == 0:
        return 'misturado'
    else:
        for a in lista:
            if a % 2 == 0:
                p += 1
            else:
                i += 1
    if p == len(lista):
        return 'par'
    elif i == len(lista):
        return 'ímpar'
    else:
        return 'misturado'