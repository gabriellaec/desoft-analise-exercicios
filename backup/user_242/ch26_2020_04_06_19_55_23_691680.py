c = float (input('Qual o valor da casa?'))
s = float (input('Qual o sálario?'))
a = float (input('Quantidade de anos a pagar?'))

if c / (a*12) > 0.3*s:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')