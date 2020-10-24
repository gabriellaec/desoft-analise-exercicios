#preço/(t*12)

preço=float(input('Qual o preço da casa a ser comprada? '))
salario=float(input('Qual o seu salario? '))
t=float(input('Em quanto tempo'))

if preço/(t*12)<=0.3*salario:
	print('Empréstimo aprovado')
else:
	print('Empréstimo não aprovado')
