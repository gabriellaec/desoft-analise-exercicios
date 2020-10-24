import math

valor=float(input('Qual o valor da conta?'))
valorC=valor*0.1 + valor
novo=round (valorC, 2)
print('Valor da conta com 10%: R$ {0}'.format(novo))