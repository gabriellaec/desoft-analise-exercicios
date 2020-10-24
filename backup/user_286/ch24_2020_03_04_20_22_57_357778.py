def calcula_aumento(salario):
    if salario > 1250:
        aumento = salario * 0.1
        print('Voce recebeu um aumento de {0}'.format(aumento))
    else:
        aumento = salario * 0.15
        print('Voce recebeu um aumento de {0}'.format(aumento))
