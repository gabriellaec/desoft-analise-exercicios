def calcula_aumento(x):
    if x > 1250:
        return  x*1.1-x
    if x <= 1250:
        return x*1.15-x
