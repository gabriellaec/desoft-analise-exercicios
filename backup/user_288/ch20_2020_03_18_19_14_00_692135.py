km_passageiro = int (input ('Quantos km deseja percorrer? ')
if km_passageiro <= 200
    preco_final = km_passageiro * 0.50
else:
	preco_final = 100 + ((km_passageiro - 200)* 0.45)
print ('Valor final da sua passagem é {0:.2f}'. format (preco_final))