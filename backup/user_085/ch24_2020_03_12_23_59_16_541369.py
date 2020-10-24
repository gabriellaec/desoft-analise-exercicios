def ccalcula_aumento(a):
    if a>=1250.00:
        a = a +(a/10)
        return a
    else:
        a = a + ((3*a)/20)
        return a