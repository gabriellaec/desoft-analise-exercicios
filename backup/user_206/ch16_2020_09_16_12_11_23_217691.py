v = input('Qual o valor da conta?')
v = float(v) * 1.1
c = round(v, 2)
print('Valor da conta com 10%: R$ {0}', format(c,".2f"))