distancia=int(input("Que distancia vc deseja percorrer?"))

if distancia>200:
	preco=distancia*0.5 + (distancia-200)*0.45
else:
    preco=distancia*0.5

print("{0:.2f}".format(preco))