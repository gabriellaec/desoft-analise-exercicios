def conta_a(texto):
    soma = 0
    i = 0
    while i < len(texto):
        if texto[i] == 'a':
            soma += 1
        i += 1
    return soma