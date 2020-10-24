nossavei=True
while nossavei:
	pergunta=int(input("Qual a velocidade do seu carro? "))
	if pergunta > 80.00:
    	multa= pergunta-80.00
    	preco=5.00*multa
    	print("Voce foi multado, no valor de R$:{:.2f}".format(preco))
	else:
        nossavei=False