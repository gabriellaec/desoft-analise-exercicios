valor=float(input('Qual o valor da conta? '))
valor_10p100=0.1*valor
valor_total=valor+valor_10p100
print('Valor da conta com 10%: R$ {0:2f}.'.format(valor_total))