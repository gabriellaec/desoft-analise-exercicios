def calcula_aumento(salario):
    if salario > 1250.00:
        salario *= 1.10
        round(salario,3)
        return ('{:.2f}'.format(salario))
    elif salario <= 1250.00:
        salario *= 1.15
        round (salario,3)
        return ('{:.2f}'.format(salario))
    