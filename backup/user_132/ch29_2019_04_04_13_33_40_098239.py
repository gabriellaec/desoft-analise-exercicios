def calcula_aumento(s):
    n= 0
    if s <= 1250:
        n = s * 1.15
    else:
        n = s * 1.1
    return n