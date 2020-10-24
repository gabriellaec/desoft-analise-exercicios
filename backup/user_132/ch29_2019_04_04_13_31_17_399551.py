def caulcula_aumento(s):
    n= 0
    if s > 1.250:
        n = s * 1.1
    else:
        n = s * 1.15
    return n