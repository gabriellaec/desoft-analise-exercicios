def calcula_aumento(salario):
    if salario > 1250:
        return 'Aumento de R$ {0}' .format(salario*0.1)
    else:
        return 'Aumento de R$ {0}' .format(salario*0.15)