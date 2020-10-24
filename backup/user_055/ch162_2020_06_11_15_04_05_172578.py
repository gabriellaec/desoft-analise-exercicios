def verifica_lista(lista_n):
    if len(lista_n) < 1:
        return 'misturado'
    for n in range(len(lista_n)):
        if lista_n[n] % 2 == 0 and lista_n[-1] % 2 == 0:
            return 'par'
        if lista_n[n] % 2 != 0 and lista_n[-1] % 2 != 0:
            return 'ímpar'
        else:
            return 'misturado'
                