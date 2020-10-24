velocidade = int(input("Digite sua velocidade: ")
if velocidade > 80:
	x = 5*(velocidade - 80)
	print("você foi multado em {0:.2f}".format(x))
else:	
	print("Não foi multado")
         