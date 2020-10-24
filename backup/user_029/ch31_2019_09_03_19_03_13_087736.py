x = int(input('valor da casa a comprar?'))
y = int(input('salario?'))
z = int(input('anos a pagar?'))
prestacao = x/(z*12)
if 0.3*y < prestacao:
    print('Empréstimo não aprovado')
if 0.3*y > prestacao:
    print('Empréstimo aprovado')
