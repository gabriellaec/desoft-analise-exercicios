def calcula_aumento(salario):
    if salario > 1250:
        print('Aumento de R$ {0}' .format(salario*0.1))
    else:
        print('Aumento de R$ {0}' .format(salario*0.15))