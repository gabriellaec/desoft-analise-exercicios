def calcula_aumento(s):
    n= 0
    if s <= 1250:
        n = s * 0.15
    else:
        n = s * 0.1
    return n