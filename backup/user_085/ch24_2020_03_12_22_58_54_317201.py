def calcula_aumento(a):
    if a>1250.00:
        a = a + (a/10)
        ff = '{:.2f}'.format(a)
        return ff
    else:
        a = a + ((a*3)/20)
        ff = '{:.2f}'.format(a)
        return ff