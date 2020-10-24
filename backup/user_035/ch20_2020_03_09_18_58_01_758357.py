passagem = int(input("Quantos km deseja percorrer? "))
if passagem <= 200:
	print("Seu preço será R${0:.2f}".format(passagem*0.5))
if passagem > 200:
	print("Seu preço será R${0:.2f}".format(100+((passagem-200)*0.45))