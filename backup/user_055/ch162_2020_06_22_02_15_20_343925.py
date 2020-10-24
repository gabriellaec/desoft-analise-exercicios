def verifica_lista(lista_n):
    if len(lista_n) < 1:
        return 'misturado'
    verifica = 0
    for n in range(len(lista_n)):
        if lista_n[n] % 2 == 0:
            verifica += 0
        else:
            verifica += 1
    if verifica == 0:
        return 'par'
    if verifica == len(lista_n):
        return 'impar'
    else:
        return 'misturado'
                