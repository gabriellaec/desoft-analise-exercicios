distancia = int(input('Quantos kilometros você deseja percorrer?'))

if distancia <= 200:
	preco = distancia * 0.5
else:
	preco = (distancia - 200) * 0.45 + (distancia * 0.5)
    
print ('R$ {:.2f}'.format(preco))            