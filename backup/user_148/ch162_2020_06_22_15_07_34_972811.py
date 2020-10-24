def verifica_lista(num):
    if len(num) == 0:
        return 'misturado'
    else:
        i = 0
        while i<len(num):
            if num[i] % 2 == 0:
                return 'par'
            elif num[i] % 2 == 1:
                return 'ímpar'
            else:
                return 'misturado'
            i += 1
