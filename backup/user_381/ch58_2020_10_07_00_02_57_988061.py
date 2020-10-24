def conta_a(n):
    soma = 0
    i = 0
    while i < len(n):
        if n[i] == 'a':
            soma += 1
        i += 1
    return soma    