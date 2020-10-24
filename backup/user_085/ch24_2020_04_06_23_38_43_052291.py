def calcula_aumento(a):
    if a > 1250.00:
        a = a * 1.10
        return '{:.2f}'.format(a)
    else:
        a = a * 1.15
        return '{:.2f}'.format(a)