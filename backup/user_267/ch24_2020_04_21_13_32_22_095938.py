def calcula_aumento(sa):
    if sa > 1250:
        aumento = 0.10*sa
    elif sa <= 1250:
        aumento = 0.15*sa
    return aumento