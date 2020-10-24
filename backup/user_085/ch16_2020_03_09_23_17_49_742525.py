c = float(input('Digite o valor da conta:'))
c = c + (c/10)
a_float = c
formatted_float = "{:.2f}".format(a_float)
print('Valor da conta com 10%: R$ {0}'.format(formatted_float))