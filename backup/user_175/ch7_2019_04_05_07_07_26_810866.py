def calcula_norma(y):
    y = list(y)
    mod = 0
    pos = 0
    while pos < len(y):
        mod = mod + ((y[pos])**2)
        pos += 1
    return 'O módulo do vetor deve ser: {0:.3f}'.format(sqrt(mod))