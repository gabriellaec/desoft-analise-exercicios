preco=int(input('valor da casa: '))
salario=int(input('salario: '))
anos=int(input('anos a pagar: '))
prestacao=preco/(anos*12)
if prestacao>=0.3*salario:
	print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')