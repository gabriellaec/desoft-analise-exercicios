def calcula_aumento(x):
    if x > 1250:
        return x + (x*10/100)
    else:
        return x + (x*15/100)