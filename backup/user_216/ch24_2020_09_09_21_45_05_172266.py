def calcula_aumento(v):
    if v > 1250:
        p = 0.1*v
    else:
        p = 0.15*v
    return p
