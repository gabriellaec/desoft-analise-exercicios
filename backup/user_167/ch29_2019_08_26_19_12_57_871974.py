def calcula_aumento (x):
    y = 0
    if x > 1250:
        y= x * 0.10
    else:
        y= x * 0.15
    return y