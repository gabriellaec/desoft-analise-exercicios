def apaga_repetidos(x):
    x = ''
    for i in x:
        if i in x:
            x += '*'
        else:
            x += i
    return x