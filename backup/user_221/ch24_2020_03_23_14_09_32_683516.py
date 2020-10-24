def calcula_aumento(salario):
    if salario > 1250:
        print(float( 'Aumento de R$ {0}' .format(salario*0.1)))
    else:
        print(float('Aumento de R$ {0}' .format(salario*0.15)))