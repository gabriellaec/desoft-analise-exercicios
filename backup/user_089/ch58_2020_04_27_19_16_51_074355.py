def conta_a(x):
    i = 0
    lista = 0
    while i <= len(x):
        if x[i] == 'a':
            lista += 1
            i += 1
        else:
            i += 1
    return lista
    