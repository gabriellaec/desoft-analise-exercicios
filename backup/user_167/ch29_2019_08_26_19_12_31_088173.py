def calcula_aumento (x):
    y = 0
    if x > 1.250:
        y= x * 1.10
    else:
        y= x * 1.15
    return y