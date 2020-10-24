salario= float(input('Digite seu salário: '))
calcula_aumento = 0.15
if salario > 1250:
    calcula_aumento = 0.10
aumento = salario * calcula_aumento
print('Seu aumento será de: R$ %7.2f' % aumento)