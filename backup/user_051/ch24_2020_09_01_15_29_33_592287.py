def calcula_aumento(x):
    if x <= 1250:
        x*=15/100
        return x
    else:
        x*=1/10
        return x