distancia = int(input('Quantos kilometros você deseja percorrer?'))

if distancia < 200:
	preco = distancia * 0.5
	print ('R$ {:.2f}'.format(preco)) 
elif distancia = 200:
    preco = distancia * 0.5
	print ('R$ {:.2f}'.format(preco)) 
else:
	precoamais = (distancia - 200) * 0.45 + (distancia * 0.5)
	print ('R$ {:.2f}'.format(precoamais))            