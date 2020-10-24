def calcula_aumento (n):
    if n > 1250:
        x = (n * 0.1) + n
        return x
    else:
        x = (n * 0.15) + n
        return x