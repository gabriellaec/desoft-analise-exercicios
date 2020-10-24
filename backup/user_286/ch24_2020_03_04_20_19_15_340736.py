salario = float(input('Qual seu salario? '))

if salario > 1250:
    aumento = format(salario*1.1 - salario, '.2f')
    print('Voce recebeu um aumento de {0}'.format(aumento))
else:
    aumento = format(salario*1.15 - salario, '.2f')
    print('Voce recebeu um aumento de {0}'.fo