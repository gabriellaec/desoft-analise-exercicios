def verifica_lista(lista):
    resp = 'misturado'
    for i in range(0,len(lista)):
        if lista[i] % 2 == 0 and resp != 'ímpar':
            resp = 'par'
        elif lista[i] % 2 != 0 and resp != 'par':
            resp = 'ímpar'
        else:
            resp = 'misturado'
    return resp