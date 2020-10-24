def calcula_aumento(s):
    if s > 1250:
        return s * 1.1 - s
    elif s <= 1250:
        return s * 1.15 - s
