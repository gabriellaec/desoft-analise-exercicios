def calcula_aumento(a):
    if a>1250.00:
        return a + (a/10)
    else:
        return a + ((3*a)/20)