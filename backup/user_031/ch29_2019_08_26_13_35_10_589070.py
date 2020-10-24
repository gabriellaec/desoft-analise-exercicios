salário = float(input('Digite seu salário:'))
calcula_aumento = 0.15
if salário > 1250:
    calcula_aumento = 0.10
aumento = salário * calcula_aumento
print('Seu aumento será de: R$ %7.2f' % aumento)