def conta_letra_a(texto):
    contador = 0
    i = 0
    n = len(texto)
    while i < n:
        if texto[i] == 'a':
            contador += 1
            i += 1
    return contador
