x = float(input('Qual o valor da casa?')
y = float(input('Qual seu salario?'))
z = float(input('Qual a quantidade de anos?'))

prestacao = x/(12*z)
if prestacao >0.3*y:
	print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
          	