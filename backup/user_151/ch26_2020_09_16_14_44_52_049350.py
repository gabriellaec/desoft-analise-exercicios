v = float(input('valor da casa '))
s = float(input('salario '))
a = float(input('anos a pagar '))

if s < 0.3*(v/(a*12)):
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')