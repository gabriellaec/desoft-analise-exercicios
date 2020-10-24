def calcula_aumento(salario):
    if salario <= 1250:
        y= salario*(15/100)
        return y
    else:
        y= salario*(10/100)
        return y
