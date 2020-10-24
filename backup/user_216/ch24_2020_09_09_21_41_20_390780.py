def calcula_aumento(v):
    if v > 1250:
        p = 1.1*v
    else:
        p = 1.15*v
    return p
