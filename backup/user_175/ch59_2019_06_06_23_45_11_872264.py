def conta_a(palavra):
    i = 0
    cont = 0
    while i < len(palavra):
        if palavra[i] == 'a':
            cont += 1
        i += 1
    return cont
        