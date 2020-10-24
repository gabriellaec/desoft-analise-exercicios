casa=int(input('valor da casa: '))
salario=int(input('salario: '))
anos_a_pagar=int(input('anos a pagar: '))
prestacao=casa/(anos_a_pagar*12)
if prestacao>=0.3*salario:
	print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')