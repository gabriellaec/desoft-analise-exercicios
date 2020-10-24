def calcula_aumento(x):
    x=float(input('salario:'))
    if x > 1250.00:
        k = x * 0.10
        y= x + k
        return 'y'
    else:
        k=x* 0.15
        y= x +k
        return 'y'