def conta_a(lista):
    S = 0
    i = 0
    while i < len(lista):
        if lista[i] == 'a':
            S += 1
        i += 1
        return S