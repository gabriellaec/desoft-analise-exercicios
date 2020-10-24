def calcula_aumento(s):
    if s > 1250:
        s *= 0.1
    elif s <= 1250:
        s *= 0.15
    return s