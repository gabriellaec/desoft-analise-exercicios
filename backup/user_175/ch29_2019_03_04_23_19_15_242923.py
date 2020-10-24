def calcula_aumento(a):
    if (0<a<=1250.00):
        res=((a)*(1.15))
    elif (a>2150.00):
        res=((a)*(1.10))
    else:
        res = 'Valor Inválido'
    return res