def verifica_lista(lista):
    for i in range(0,len(lista)):
        if lista[i] % 2 == 0 and resp != 'impar':
            resp = 'par'
        elif lista[i] % 2 != 0 and resp != 'par':
            resp = 'impar'
        else:
            resp = 'misturado'
    return resp