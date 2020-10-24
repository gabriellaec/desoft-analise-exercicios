def verifica_lista(lista_n):
    if len(lista_n) < 1:
        return 'misturado'
    for n in lista_n:
        if all(n % 2 == 0):
            return 'par'
        if all(n % 2 != 0):
            return 'ímpar'
        else:
            return 'misturado'
                