v = float(input('valor da casa '))
s = float(input('salario '))
a = float(input('anos a pagar '))

if s < (v/(a*12))/0.3:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')