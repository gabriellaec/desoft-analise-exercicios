def calcula_aumento(x):
    if int(x) >= 1250:
        k = (x * 10)/100
        y= x + k
        return 'y'
    else:
        k=(x* 15)/100
        y= x +k
        return 'y'