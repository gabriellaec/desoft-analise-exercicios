def calcula_aumento (n):
    if n <= 1250:
        x = n + (n * 0.15)
        return x
    else:
        x = n + (n * 0.10)
        return x