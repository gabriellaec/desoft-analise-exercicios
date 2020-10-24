def f(y):
     x = y*1.1
     return x

y = float(input('Qual é o valor total da conta?'))
total = f(y)
print('Valor da conta com 10%: R${:.2f}'.format(total))