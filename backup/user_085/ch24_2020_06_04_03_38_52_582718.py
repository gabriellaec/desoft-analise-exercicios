def calcula_aumento(salario):
    if salario > 1250.00:
        salario *= 1.10
        round(salario,3)
        s = '{:.2f}'.format(salario)
        type(float(s))
        return s
    elif salario <= 1250.00:
        salario *= 1.15
        s = ('{:.2f}'.format(salario))
        type(float(s))
        return s