def conta_a(x):
    i = 0
    contador = 0
    if len(x) == 0:
        return 0
    else:
        while(i <= len(x)):
            if x[i] == 'a':
                contador += 1
            i += 1
        return contador