def conta_a(x):
    i = 0
    contador = 0
    x = str(x)
    while i < len(x):
            if x[i] == 'a':
                contador += 1
                i +=1
            else:
                i += 1
    return contador