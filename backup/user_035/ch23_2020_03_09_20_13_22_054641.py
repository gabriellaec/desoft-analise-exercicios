velocidade_do_carro = int(input("Qual é a velocidade do carro do usuário"))
if velocidade_do_carro>80:
	print("O carro foi multado por R${0:.2f}".format((velocidade_do_carro-80)*5)
else:
	print("Não foi multado")