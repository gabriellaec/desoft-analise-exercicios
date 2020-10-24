def calcula_aumento(x):
    x=float(input('salario:'))
    if x >= 1250.00:
        k = (x * 10)/100
        y= x + k
        return 'y'
    else:
        k=(x* 15)/100
        y= x +k
        return 'y'