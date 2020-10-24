def calcula_aumento(salario):
    if salario > 1250:
        aumento = salario * 1.1 - salario
        print('Voce recebeu um aumento de {0}'.format(aumento))
    else:
        aumento = salario * 1.15 - salario
        print('Voce recebeu um aumento de {0}'.format(aumento))
