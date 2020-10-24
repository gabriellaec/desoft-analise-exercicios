def inverte_lista(LISTA):
    LISTA_invertida = []
    t = 0
    a = len(LISTA)
    while t < a:
        LISTA_invertida.append(LISTA[-1])
        del(LISTA[-1])
        t += 1
    return LISTA_invertida
