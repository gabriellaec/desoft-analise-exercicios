def verifica_lista(num):
    if len(num) == 0:
        return 'misturado'
    for n in num:
        if n % 2 == 0:
            return 'par'
        elif n % 2 == 1:
            return 'impar'
        else:
            return 'misturado'
