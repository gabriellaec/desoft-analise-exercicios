def calcula_aumento(x):
    if float(x) > 1250:
        return float(0.1*1250)
    else:
        return float(0.15*x)
    