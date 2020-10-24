def cobranca(distancia):
    if distancia < 200:
        preco=0.5*200
	else:
        preco=200+0.45*(distancia-200)
	return preco
distancia=int(input("Fale uma distancia: ")
print (cobranca(distancia))