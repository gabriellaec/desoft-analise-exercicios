def conta_a(texto):
    i = 0
    contador = 0
    n = len(texto)
    while i < n:
        if texto[i] == 'a':
            contador += 1
        i += 1
    return contador
            