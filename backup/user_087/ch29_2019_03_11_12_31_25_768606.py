def calcula_aumento(x):
    if float(x) > 1250:
        return float(0.1*float(x))
    else:
        return float(0.15*float(x))
    