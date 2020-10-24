def calcula_norma(y):
    y = list(y)
    mod = 0
    pos = 0
    while pos <= len(y):
        mod = mod + ((y[pos])**2)
        pos += 1
    return mod