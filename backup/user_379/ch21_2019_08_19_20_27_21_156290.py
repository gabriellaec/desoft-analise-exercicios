def calcula_conta(pergunta):
	y=pergunta*1.1
	return y
pergunta=float(input("digite o valor da conta: "))
print("valor da conta com 10%: R${0:.2f}".format(calcula_conta(pergunta)))