def calcula_aumento(v):
    if v > 1250:
        aumento = 0.1*v
    else:
        aumento = 0.15*v
    return aumento