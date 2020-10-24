def calcula_aumento(x):
    if x > 1250:
        y = x*(0.1)
    elif x <= 1250:
        y = x*(0.15)
    return y