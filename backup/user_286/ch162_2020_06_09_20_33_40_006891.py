def verifica_lista(lista):
    i = 0
    p = 0
    for num in lista:
        if num % 2 == 0:
            p += 1
        else:
            i += 1
    
    if p == 0:
        return 'ímpar'
    elif i == 0:
        return 'par'
    else:
        return 'misturado'